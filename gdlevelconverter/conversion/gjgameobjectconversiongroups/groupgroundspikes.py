"""
Ground spike group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupGroundSpikes = GJGameObjectConversionGroup(
    "ground_spikes",
    [
        GJGameObjectConversion(1711, 135),
        GJGameObjectConversion(1712, 135),
        GJGameObjectConversion(1713, 135),
        GJGameObjectConversion(1714, 135),
    ],
    show_hitbox_warning=True,
    show_visual_warning=True,
)
