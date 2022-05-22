"""
Defines conversions for the colors in level settings
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class LevelSettingsColorConversion():
    """
    Defines a conversion between color index and key
    """
    color_index: int
    header_key: str


LevelSettingsColorConversions: List[LevelSettingsColorConversion] = [
    LevelSettingsColorConversion(1, "color_1"),
    LevelSettingsColorConversion(2, "color_2"),
    LevelSettingsColorConversion(3, "color_3"),
    LevelSettingsColorConversion(4, "color_4"),
    LevelSettingsColorConversion(1000, "color_bg"),
    LevelSettingsColorConversion(1001, "color_ground"),
    LevelSettingsColorConversion(1002, "color_line"),
    LevelSettingsColorConversion(1003, "color_3dl"),
    LevelSettingsColorConversion(1004, "color_object"),
]
