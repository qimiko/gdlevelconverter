"""
Slab group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupSlabs = GJGameObjectConversionGroup(
    "slabs",
    [
        GJGameObjectConversion(1260, 468),
        GJGameObjectConversion(1903, 40),
        GJGameObjectConversion(1904, 369),
        GJGameObjectConversion(1905, 370),
        GJGameObjectConversion(1910, 195),
        GJGameObjectConversion(1911, 196),
    ],
)
