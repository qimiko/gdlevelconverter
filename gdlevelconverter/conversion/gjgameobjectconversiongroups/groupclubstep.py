"""
Clubstep block group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupClubstep = GJGameObjectConversionGroup(
    "clubstep",
    [
        GJGameObjectConversion(1140, 162),
        GJGameObjectConversion(1141, 163),
        GJGameObjectConversion(1143, 165),
        GJGameObjectConversion(1144, 166),
        GJGameObjectConversion(1145, 167),
        GJGameObjectConversion(1146, 168),
        GJGameObjectConversion(1147, 169),
    ],
    show_hitbox_warning=True,
)
