"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Generic, TypeVar, List, Dict

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup import GJGameObjectConversionGroup


# hacky circular import fix
T = TypeVar("T")


@dataclass
class ConversionReport(Generic[T]):
    """
    Options during full level conversion
    """
    converted_triggers: List[T]
    group_conversions: Dict[GJGameObjectConversionGroup, List[T]]
    removed_objects: List[T]
    preconversion_object_count: int
