"""
Pillar block group for id conversion
"""

from .gjgameobjectconversiongroup import GJGameObjectConversion, GJGameObjectConversionGroup


GroupPillars = GJGameObjectConversionGroup(
    "pillars",
    [
        GJGameObjectConversion(1737, 668),
        GJGameObjectConversion(1738, 669),
        GJGameObjectConversion(1739, 670),
        GJGameObjectConversion(1740, 671),
        GJGameObjectConversion(1741, 672),
        GJGameObjectConversion(1742, 738)
    ],
    show_visual_warning=True
)
