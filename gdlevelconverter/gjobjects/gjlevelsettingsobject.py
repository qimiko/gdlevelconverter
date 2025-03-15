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
            key="audio_track", index="kA1", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="start_gamemode", index="kA2", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="start_mini", index="kA3", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="start_speed", index="kA4", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col1_blend", index="kA5", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="background_id", index="kA6", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="ground_id", index="kA7", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="start_dual", index="kA8", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="start_pos", index="kA9", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="two_player", index="kA10", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="start_flipped", index="kA11", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col3_blend", index="kA12", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="song_offset", index="kA13", deserialize_as=float
        ),
        gjdictionary.ObjectDefinition(
            key="guidelines", index="kA14", deserialize_as=str
        ),
        gjdictionary.ObjectDefinition(key="fade_in", index="kA15", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="fade_out", index="kA16", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="legacy_bg_r", index="kS1", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_bg_g", index="kS2", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_bg_b", index="kS3", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_ground_r", index="kS4", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_ground_g", index="kS5", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_ground_b", index="kS6", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_line_r", index="kS7", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_line_g", index="kS8", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_line_b", index="kS9", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_obj_r", index="kS10", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_obj_g", index="kS11", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_obj_b", index="kS12", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col1_r", index="kS13", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col1_g", index="kS14", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col1_b", index="kS15", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_bg_custom", index="kS16", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_ground_custom", index="kS17", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_line_custom", index="kS18", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_obj_custom", index="kS19", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col1_custom", index="kS20", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col2_r", index="kS21", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col2_g", index="kS22", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col2_b", index="kS23", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col3_r", index="kS24", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col3_g", index="kS25", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col3_b", index="kS26", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="legacy_col2_custom", index="kS28", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_bg", index="kS29", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_ground", index="kS30", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_line", index="kS31", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_object", index="kS32", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_1", index="kS33", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_2", index="kS34", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_3", index="kS35", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_4", index="kS36", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_3dl", index="kS37", deserialize_as=GJColorObject
        ),
        gjdictionary.ObjectDefinition(
            key="color_list",
            index="kS38",
            deserialize_as=gjdictionary.as_list(GJColorObject, "|"),
            serialize_as=gjdictionary.from_list("|"),
        ),
    ]

    _splitter = ","

    audio_track: Optional[int]
    start_gamemode: Optional[int]
    start_mini: Optional[int]
    start_speed: Optional[int]
    legacy_col1_blend: Optional[int]
    background_id: Optional[int]
    ground_id: Optional[int]
    start_dual: Optional[int]
    start_pos: Optional[int]
    two_player: Optional[int]
    start_flipped: Optional[int]
    legacy_col3_blend: Optional[int]
    song_offset: Optional[float]
    guidelines: Optional[str]
    fade_in: Optional[int]
    fade_out: Optional[int]

    legacy_bg_r: Optional[int]
    legacy_bg_g: Optional[int]
    legacy_bg_b: Optional[int]
    legacy_ground_r: Optional[int]
    legacy_ground_g: Optional[int]
    legacy_ground_b: Optional[int]
    legacy_line_r: Optional[int]
    legacy_line_g: Optional[int]
    legacy_line_b: Optional[int]
    legacy_obj_r: Optional[int]
    legacy_obj_g: Optional[int]
    legacy_obj_b: Optional[int]
    legacy_col1_r: Optional[int]
    legacy_col1_g: Optional[int]
    legacy_col1_b: Optional[int]
    legacy_bg_custom: Optional[int]
    legacy_ground_custom: Optional[int]
    legacy_line_custom: Optional[int]
    legacy_obj_custom: Optional[int]
    legacy_col1_custom: Optional[int]
    legacy_col2_r: Optional[int]
    legacy_col2_g: Optional[int]
    legacy_col2_b: Optional[int]
    legacy_col3_r: Optional[int]
    legacy_col3_g: Optional[int]
    legacy_col3_b: Optional[int]
    legacy_col2_custom: Optional[int]

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
                setattr(
                    self, conversion.header_key, channel_dict[conversion.color_index]
                )

        # clear new color list
        del self.color_list
        return True
