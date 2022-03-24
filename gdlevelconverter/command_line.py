"""
Main CLI script for the Geometry Dash level conversion tool
"""

import argparse
import collections
from pathlib import Path

from .gjobjects import GJClient, GJGameLevel
from . import ConversionReport, ConversionOptions
from . import GJGameObjectConversionGroupsByName, GJGameObjectConversionSubGroups


def load_level_from_target(target: str):
    """
    Loads a level given either a path or id
    """
    level = GJGameLevel()

    path = Path(target)
    if path.is_file():
        print(f"Loading level from file `{target}`")

        gmd_string = ""
        with open(path, "r", encoding="utf-8") as gmd:
            gmd_string = gmd.read()

        if not gmd_string:
            raise ValueError("Blank file passed for .gmd")

        level = GJGameLevel.from_gmd(gmd_string)
    elif target.isdigit():
        level_id = int(target)
        print(f"Downloading level {level_id}")

        client = GJClient(game_version=21)
        level = GJGameLevel.from_id(client, level_id)
    else:
        raise ValueError("invalid value for target passed")

    return level


def parse_group_conversion(conversion_report: ConversionReport):
    """
    Returns string output for group conversion report
    """
    output = ""

    used_groups = [
        k for (k, v) in conversion_report.group_conversions.items() if v]

    if used_groups:
        output += "Object id conversions by group:\n"
        total_count = 0
        group_conversion_counts = {k.name: len(v) for (k, v)
                                   in conversion_report.group_conversions.items() if v}

        for (group_name, count) in group_conversion_counts.items():
            converted_percentage = count * 100 / conversion_report.preconversion_object_count
            output += f"{group_name} - {count}x ({converted_percentage:.2f}%)\n"
            total_count += count

        converted_percentage = total_count * \
            100 / conversion_report.preconversion_object_count
        output += f"total - {total_count}x ({converted_percentage:.2f}%)\n"

        show_hitbox_warning = [
            x.name for x in used_groups if x.show_hitbox_warning]
        if show_hitbox_warning:
            output += f"Group(s) `{', '.join(show_hitbox_warning)}` may impact level hitboxes, \
potentially making the level impossible.\n"

        show_visual_warning = [
            x.name for x in used_groups if x.show_visual_warning]
        if show_visual_warning:
            output += f"Group(s) `{', '.join(show_visual_warning)}` \
may heavily impact level visuals, \
potentially worsening the playing experience.\n"

    return output


def parse_removed_report(conversion_report: ConversionReport):
    """
    Parses removed object report to string
    """

    output = ""

    if conversion_report.removed_objects:
        output += "Illegal objects:\n"

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


def _main():
    """
    Main function for script
    """

    group_choices = list(GJGameObjectConversionGroupsByName) + \
        list(GJGameObjectConversionSubGroups)

    parser = argparse.ArgumentParser(
        description="Geometry Dash 2.0+ to 1.9 Level Converter",
        epilog="hi ~zmx",
    )

    parser.add_argument("target", help="path to .gmd file or level id")
    parser.add_argument(
        "-g", "--groups", help="groups for use in id conversion. selects base subgroup by default",
        nargs="*", choices=group_choices, default=["base"]
    )
    parser.add_argument("-o", "--output",
                        help=".gmd file name to output to. use - to upload to servers")

    args = parser.parse_args()

    level = load_level_from_target(args.target)

    print(f"Running conversion on level `{level.name}`")
    print(f"Original object count - {len(level.level_string.objects)} objects")

    print()

    groups = []

    for group in args.groups:
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

    group_report = parse_group_conversion(conversion_report)
    if group_report:
        print(group_report)

    removed_report = parse_removed_report(conversion_report)
    print(removed_report)

    if args.output == "-":
        print("Uploading level to 1.9 servers")

        client = GJClient(
            game_version=19, upload_url="https://absolllute.com/gdps/gdapi/uploadGJLevel19.php")

        resp_id = level.upload(client)

        print(f"Level uploaded to id {resp_id}")

        return

    if args.output:
        print(f"Saving to file `{args.output}`")

        gmd_output = level.to_gmd()

        with open(args.output, "w", encoding="utf-8") as gmd:
            gmd.write(gmd_output)

    print("Finished!")
