"""
Remaining trigger block group for id conversion
"""

from .gjgameobjectconversiongroup import (
    GJGameObjectConversion,
    GJGameObjectConversionGroup,
)


GroupTriggers = GJGameObjectConversionGroup(
    "misc_triggers",
    [
        GJGameObjectConversion(915, 104),
    ],
)
