"""
Circle block group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupCircle = GJGameObjectConversionGroup(
    "circle", [GJGameObjectConversion(1764, 725)], show_visual_warning=True
)
