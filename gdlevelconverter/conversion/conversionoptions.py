"""
Defines conversion options class
"""
from dataclasses import dataclass

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup import (
    GJGameObjectConversionGroup,
)


@dataclass
class ConversionOptions:
    """
    Options during full level conversion
    """

    groups: list[GJGameObjectConversionGroup]
    conv_white: bool = False
    maximum_id: int | None = None
