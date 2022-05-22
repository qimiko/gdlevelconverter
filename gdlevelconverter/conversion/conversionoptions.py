"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Optional, List

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup \
    import GJGameObjectConversionGroup


@dataclass
class ConversionOptions:
    """
    Options during full level conversion
    """
    groups: List[GJGameObjectConversionGroup]
    maximum_id: Optional[int] = None
