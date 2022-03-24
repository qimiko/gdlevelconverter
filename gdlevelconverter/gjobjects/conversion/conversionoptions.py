"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Optional

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup \
    import GJGameObjectConversionGroup


@dataclass
class ConversionOptions:
    """
    Options during full level conversion
    """
    groups: list[GJGameObjectConversionGroup]
    maximum_id: Optional[int] = None
