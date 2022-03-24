"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Generic, TypeVar

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup import GJGameObjectConversionGroup


# hacky circular import fix
TYPE = TypeVar("TYPE")


@dataclass
class ConversionReport(Generic[TYPE]):
    """
    Options during full level conversion
    """
    converted_triggers: list[TYPE]
    group_conversions: dict[GJGameObjectConversionGroup, list[TYPE]]
    removed_objects: list[TYPE]
    preconversion_object_count: int
