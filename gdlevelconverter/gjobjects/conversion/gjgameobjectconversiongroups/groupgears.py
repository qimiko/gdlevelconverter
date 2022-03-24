"""
Gear object group for id conversion
"""

from .gjgameobjectconversiongroup import GJGameObjectConversion, GJGameObjectConversionGroup


GroupGears = GJGameObjectConversionGroup(
    "gears",
    [
        GJGameObjectConversion(1705, 88),
        GJGameObjectConversion(1706, 89),
        GJGameObjectConversion(1707, 98),
        GJGameObjectConversion(1708, 397),
        GJGameObjectConversion(1709, 398),
        GJGameObjectConversion(1710, 399),
        GJGameObjectConversion(1734, 675),
        GJGameObjectConversion(1735, 676),
        GJGameObjectConversion(1736, 677),
    ],
)
