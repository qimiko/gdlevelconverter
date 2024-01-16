"""
Main CLI script for the Geometry Dash level conversion tool
"""

import argparse
import collections
from importlib.metadata import version
from pathlib import Path

from .gjobjects import GJClient, GJGameLevel
from .conversion import ConversionReport, ConversionOptions
from .conversion import GJGameObjectConversionGroupsByName, GJGameObjectConversionSubGroups


def load_level_from_target(target: str):
    """
    Loads a level given either a path or id
    """
    level = GJGameLevel()

    path = Path(target)
    if path.is_file():
        print(f"Loading level from file `{target}`")

        gmd_string = ""

        # sometimes gmd files can get some corruption after the level string
        # ignoring errors may break if the corruption happens to be utf8 shaped
        with open(path, "r", encoding="utf-8", errors="ignore") as gmd:
            gmd_string = gmd.read()

        if not gmd_string:
            raise ValueError("Blank file passed for .gmd")

        level = GJGameLevel.from_gmd(gmd_string)
    elif target.isdigit():
        level_id = int(target)
        print(f"Downloading level {level_id}")

        client = GJClient(game_version=22, binary_version=38)
        level = GJGameLevel.from_id(client, level_id)
    else:
        raise ValueError("invalid value for target passed")

    return level


def parse_group_conversion(conversion_report: ConversionReport, verbose: bool = False):
    """
    Returns string output for group conversion report
    """
    output = ""

    used_groups = [
        k for (k, v) in conversion_report.group_conversions.items() if v]

    if used_groups:
        output += "Object id conversions by group:\n"
        total_count = 0
        group_conversion_counts = {k: len(v) for (k, v)
                                   in conversion_report.group_conversions.items() if v}

        for (group, count) in group_conversion_counts.items():
            converted_percentage = count * 100 / conversion_report.preconversion_object_count
            output += f"{group.name} - {count}x ({converted_percentage:.2f}%)\n"
            total_count += count

            if verbose:
                for obj in conversion_report.group_conversions[group]:
                    output += f"object {obj.object_id} at \
(x: {obj.x_position:g}, y: {obj.y_position:g})\n"
                output += "\n"

        converted_percentage = total_count * \
            100 / conversion_report.preconversion_object_count
        output += f"total - {total_count}x ({converted_percentage:.2f}%)\n"

        show_hitbox_warning = [
            x.name for x in used_groups if x.show_hitbox_warning]
        if show_hitbox_warning:
            output += f"Group(s) `{', '.join(show_hitbox_warning)}` may impact level hitboxes. \
This can make the level impossible.\n"

        show_visual_warning = [
            x.name for x in used_groups if x.show_visual_warning]
        if show_visual_warning:
            output += f"Group(s) `{', '.join(show_visual_warning)}` \
may impact level visuals.\n"

    return output


def parse_removed_report(conversion_report: ConversionReport, verbose: bool = False):
    """
    Parses removed object report to string
    """

    output = ""

    if conversion_report.removed_objects:
        output += "Illegal objects:\n"

        if verbose:
            for obj in conversion_report.removed_objects:
                output += f"object {obj.object_id} at \
(x: {obj.x_position:g}, y: {obj.y_position:g})\n"
            output += "\n"
        else:
            # simplify output to be based on frequency of object ids
            removed_ids = [x.object_id for x in conversion_report.removed_objects]
            removed_freq = collections.Counter(removed_ids)

            for (removed_id, count) in removed_freq.items():
                removed_percentage = count * 100 / conversion_report.preconversion_object_count
                output += f"object {removed_id} - {count}x ({removed_percentage:.2f}%)\n"

        removed_count = len(conversion_report.removed_objects)
        removed_percentage = removed_count * \
            100 / conversion_report.preconversion_object_count
        output += f"total - {removed_count} objects removed ({removed_percentage:.2f}%)\n"
    else:
        output += "No objects removed.\n"

    return output


def parse_reports(conversion_report: ConversionReport, verbose: bool = False):
    """
    Parses all reports into one string
    """

    output = ""

    group_report = parse_group_conversion(conversion_report, verbose)
    if group_report:
        output += group_report + "\n"

    removed_report = parse_removed_report(conversion_report, verbose)
    output += removed_report

    return output


def _main():
    """
    Main function for script
    """

    group_choices = list(GJGameObjectConversionGroupsByName) + \
        list(GJGameObjectConversionSubGroups) + ["none"]

    parser = argparse.ArgumentParser(
        description="Geometry Dash 2.0+ to 1.9 Level Converter",
        epilog="hi ~zmx",
    )

    parser.add_argument("target", help="path to .gmd file or level id")
    parser.add_argument(
        "-g", "--groups",
        help="groups for use in id conversion. selects base subgroup by default. \
use none to disable id conversion",
        nargs="*", choices=group_choices, default=["base"]
    )
    parser.add_argument("-o", "--output",
                        help=".gmd file name to output to. use - to upload to servers")
    parser.add_argument(
        '--verbose', help="enables extra logging", action="store_true")
    parser.add_argument('-v', '--version', action='version', version=version('gdlevelconverter'))

    args = parser.parse_args()

    level = load_level_from_target(args.target)

    print(f"Running conversion on level `{level.name}`")
    print(f"Original object count - {len(level.level_string.objects)} objects")

    print()

    groups = []

    for group in args.groups:
        if group == "none":
            if len(args.groups) > 1:
                print("Selecting no groups conflicts with selecting groups")
                return
            continue

        if group in GJGameObjectConversionSubGroups:
            groups.extend(GJGameObjectConversionSubGroups[group])
            continue

        if group in GJGameObjectConversionGroupsByName:
            groups.append(GJGameObjectConversionGroupsByName[group])
        else:
            print(
                f"Invalid group, possible groups are {group_choices}")
            return

    # as of right now the target version is hardcoded
    conversion_report = level.level_string.to_legacy_format(
        ConversionOptions(
            groups=groups,
            maximum_id=744
        )
    )
    level.binary_version = 24

    reports = parse_reports(conversion_report, args.verbose)
    print(reports)

    if args.output == "-":
        print("Uploading level to 1.9 servers")

        client = GJClient(
            game_version=19, binary_version=24,
            upload_url="https://absolllute.com/gdps/gdapi/uploadGJLevel19.php"
        )

        resp_id = level.upload(client)

        print(f"Level uploaded to id {resp_id}")

        return

    if args.output:
        print(f"Saving to file `{args.output}`")

        gmd_output = level.to_gmd()

        with open(args.output, "w", encoding="utf-8") as gmd:
            gmd.write(gmd_output)

    print("Finished!")
