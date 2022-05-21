"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Generic, TypeVar, List, Dict

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup import GJGameObjectConversionGroup


# hacky circular import fix
TYPE = TypeVar("TYPE")


@dataclass
class ConversionReport(Generic[TYPE]):
    """
    Options during full level conversion
    """
    converted_triggers: List[TYPE]
    group_conversions: Dict[GJGameObjectConversionGroup, List[TYPE]]
    removed_objects: List[TYPE]
    preconversion_object_count: int
