"""
Defines GJLevelString class
"""

import base64
import gzip
import zlib
from typing import List
from ..conversion.conversionoptions import ConversionOptions
from ..conversion.conversionreport import ConversionReport
from .gjgameobject import GJGameObject
from .gjlevelsettingsobject import GJLevelSettingsObject


class GJLevelString:
    """
    Deserialized representation of a Geometry Dash level string
    """

    OBJECT_SEPARATOR: str = ";"

    header: GJLevelSettingsObject
    objects: List[GJGameObject]

    def __init__(self, level):
        object_strings = level.split(self.OBJECT_SEPARATOR)
        header_string = object_strings.pop(0)

        self.objects = [GJGameObject(x) for x in object_strings if x]
        self.header = GJLevelSettingsObject(header_string)

    def to_legacy_format(self, conversion_options: ConversionOptions):
        """
        Converts level to legacy (1.9) format
        """

        # step 1, convert header
        self.header.to_legacy_format()

        # step 2, convert objects
        report = ConversionReport[GJGameObject](
            converted_triggers=[],
            group_conversions={x: [] for x in conversion_options.groups},
            removed_objects=[],
            preconversion_object_count=len(self.objects),
        )

        for obj in self.objects:
            if obj.object_id == GJGameObject.UNIFIED_COLOR_TRIGGER_ID:
                if obj.remap_to_legacy_id_by_target():
                    report.converted_triggers.append(obj)
            else:
                # as of rn i don't bother tracking this value
                obj.to_legacy_color(conversion_options.conv_white)
                group_result = obj.remap_to_legacy_id_by_groups(
                    conversion_options.groups
                )
                if group_result:
                    report.group_conversions[group_result].append(obj)

        # step 3, filter out objects that shouldn't exist (if enabled)
        if conversion_options.maximum_id:
            # this is very inefficient...
            filtered_objects = []
            for obj in self.objects:
                # keep only objects below maximum id
                if obj.object_id <= conversion_options.maximum_id:
                    filtered_objects.append(obj)
                else:
                    report.removed_objects.append(obj)

            self.objects = filtered_objects

        return report

    @classmethod
    def from_encoded(cls, level: str):
        """
        Builds an instance of a level from an encoded string
        """
        if level.startswith("kS") or level.startswith("kA"):
            return cls(level)

        # convert level to ascii beforehand so errors can be ignored
        level_ascii = level.encode("ascii", errors="ignore")
        level_zipped = base64.urlsafe_b64decode(level_ascii)

        # fallback in case conversion fails
        level_unzipped = level_zipped

        try:
            level_unzipped = gzip.decompress(level_zipped)
        except gzip.BadGzipFile:
            level_unzipped = zlib.decompress(level_zipped)

        return cls(level_unzipped.decode())

    def __to_object_string(self):
        object_string = (
            self.OBJECT_SEPARATOR.join([str(x) for x in self.objects])
            + self.OBJECT_SEPARATOR
        )

        return f"{self.header}{self.OBJECT_SEPARATOR}{object_string}"

    def to_encoded(self):
        """
        Encodes the level string to save data format
        """
        return base64.urlsafe_b64encode(
            gzip.compress(self.__to_object_string().encode())
        ).decode()

    def __str__(self):
        return self.__to_object_string()
