"""
Decoration block group for id conversion
"""

from .gjgameobjectconversiongroup import GJGameObjectConversion, GJGameObjectConversionGroup


GroupDecoration = GJGameObjectConversionGroup(
    "decoration",
    [
        GJGameObjectConversion(1142, 164),
        GJGameObjectConversion(1148, 193),
        GJGameObjectConversion(1825, 251),
        GJGameObjectConversion(1889, 191),
        GJGameObjectConversion(1890, 198),
        GJGameObjectConversion(1891, 199),
        GJGameObjectConversion(1892, 393),
    ],
)
