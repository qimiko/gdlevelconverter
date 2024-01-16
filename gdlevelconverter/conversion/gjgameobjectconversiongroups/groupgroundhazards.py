"""
Ground hazard group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupGroundHazards = GJGameObjectConversionGroup(
    "ground_hazards",
    [
        GJGameObjectConversion(1715, 9),
        GJGameObjectConversion(1716, 365),
        GJGameObjectConversion(1717, 363),
        GJGameObjectConversion(1718, 364),
        GJGameObjectConversion(1719, 61),
        GJGameObjectConversion(1720, 243),
        GJGameObjectConversion(1721, 244),
        GJGameObjectConversion(1722, 368),
        GJGameObjectConversion(1723, 366),
        GJGameObjectConversion(1724, 367),
        GJGameObjectConversion(1725, 421),
        GJGameObjectConversion(1726, 422),
        GJGameObjectConversion(1728, 446),
        GJGameObjectConversion(1729, 447),
        GJGameObjectConversion(1730, 667),
        GJGameObjectConversion(1731, 720),
    ],
)
