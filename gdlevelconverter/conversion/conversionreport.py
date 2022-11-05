"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Generic, TypeVar, List, Dict

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup import GJGameObjectConversionGroup


# hacky circular import fix
ObjectType = TypeVar("ObjectType")


@dataclass
class ConversionReport(Generic[ObjectType]):
    """
    Options during full level conversion
    """
    converted_triggers: List[ObjectType]
    group_conversions: Dict[GJGameObjectConversionGroup, List[ObjectType]]
    removed_objects: List[ObjectType]
    preconversion_object_count: int
