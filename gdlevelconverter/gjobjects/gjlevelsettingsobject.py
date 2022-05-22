"""
Definition for GJLevelSettingsObject
"""

from typing import Optional, List

from ..conversion import LevelSettingsColorConversions
from .gjcolorobject import GJColorObject
from . import gjdictionary


class GJLevelSettingsObject(gjdictionary.GJDictionary):
    """
    Deserialized representation of Geometry Dash LevelSettingsObject
    """
    _definitions = [
        gjdictionary.ObjectDefinition(
            key="color_bg", index="kS29", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_ground", index="kS30", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_line", index="kS31", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_object", index="kS32", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_1", index="kS33", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_2", index="kS34", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_3", index="kS35", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_4", index="kS36", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_3dl", index="kS37", deserialize_as=GJColorObject),
        gjdictionary.ObjectDefinition(
            key="color_list", index="kS38",
            deserialize_as=gjdictionary.as_list(GJColorObject, "|"),
            serialize_as=gjdictionary.from_list("|")),
    ]

    _splitter = ","

    color_bg: Optional[GJColorObject]
    color_ground: Optional[GJColorObject]
    color_line: Optional[GJColorObject]
    color_object: Optional[GJColorObject]
    color_1: Optional[GJColorObject]
    color_2: Optional[GJColorObject]
    color_3: Optional[GJColorObject]
    color_4: Optional[GJColorObject]
    color_3dl: Optional[GJColorObject]

    color_list: Optional[List[GJColorObject]]

    def to_legacy_format(self) -> bool:
        """
        Converts level header to legacy 1.9 format
        Returns True if conversion was performed
        """

        if not hasattr(self, "color_list"):
            return False

        channel_dict = {x.channel: x for x in self.color_list}

        for conversion in LevelSettingsColorConversions:
            if conversion.color_index in channel_dict:
                setattr(self, conversion.header_key,
                        channel_dict[conversion.color_index])

        # clear new color list
        del self.color_list
        return True
