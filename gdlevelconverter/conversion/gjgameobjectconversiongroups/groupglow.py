"""
Full glow block group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupGlow = GJGameObjectConversionGroup(
    "glow",
    [
        GJGameObjectConversion(1011, 503),
        GJGameObjectConversion(1012, 504),
        GJGameObjectConversion(1013, 505),
    ],
    show_visual_warning=True,
)
