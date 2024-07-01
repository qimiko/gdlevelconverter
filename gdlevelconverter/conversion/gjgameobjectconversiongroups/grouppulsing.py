"""
Pulsing object group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupPulsing = GJGameObjectConversionGroup(
    "pulsing",
    [
        GJGameObjectConversion(3621, 50), # small circle
        GJGameObjectConversion(3622, 51), # small circle outline
        GJGameObjectConversion(3623, 52), # heart
        GJGameObjectConversion(3624, 53), # diamond
        GJGameObjectConversion(3625, 54), # star
        GJGameObjectConversion(3626, 60), # music note
        GJGameObjectConversion(3627, 148), # square
        GJGameObjectConversion(3628, 149), # triangle
        GJGameObjectConversion(3629, 405), # hexagon
        GJGameObjectConversion(3630, 132), # arrow (->)
        GJGameObjectConversion(3631, 460), # right angle (›)
        GJGameObjectConversion(3632, 494), # right facing triangle (▶)
        GJGameObjectConversion(3633, 133), # exclamation mark
        GJGameObjectConversion(3634, 136), # question mark
        GJGameObjectConversion(3635, 150), # large x
        GJGameObjectConversion(3636, 236), # large circle outline
        GJGameObjectConversion(3637, 497), # large circle
        GJGameObjectConversion(3638, 495), # large square
        GJGameObjectConversion(3639, 496), # large square outline
    ],
    show_visual_warning=True,
)
