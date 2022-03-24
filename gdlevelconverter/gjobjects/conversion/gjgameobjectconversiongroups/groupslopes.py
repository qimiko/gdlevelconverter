"""
Slope block group for id conversion
"""

from .gjgameobjectconversiongroup import GJGameObjectConversion, GJGameObjectConversionGroup


GroupSlopes = GJGameObjectConversionGroup(
    "slopes",
    [
        GJGameObjectConversion(1743, 289),
        GJGameObjectConversion(1744, 291),
        GJGameObjectConversion(1745, 299),
        GJGameObjectConversion(1746, 301),
        GJGameObjectConversion(1747, 309),
        GJGameObjectConversion(1748, 311),
        GJGameObjectConversion(1749, 315),
        GJGameObjectConversion(1750, 317),
        GJGameObjectConversion(1338, 665),
        GJGameObjectConversion(1339, 666),
        GJGameObjectConversion(1906, 371),
        GJGameObjectConversion(1907, 372),
        GJGameObjectConversion(1908, 373),
        GJGameObjectConversion(1909, 374),
    ],
    show_visual_warning=True
)
