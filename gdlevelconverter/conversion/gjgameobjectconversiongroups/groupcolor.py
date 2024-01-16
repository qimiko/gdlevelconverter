"""
Default color block group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupColor = GJGameObjectConversionGroup(
    "color",
    [
        GJGameObjectConversion(1820, 247),
        GJGameObjectConversion(1821, 248),
        GJGameObjectConversion(1823, 249),
        GJGameObjectConversion(1824, 250),
        GJGameObjectConversion(1826, 252),
        GJGameObjectConversion(1827, 253),
        GJGameObjectConversion(1828, 254),
    ],
    show_hitbox_warning=True,
)
