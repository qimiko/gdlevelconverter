"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Generic, TypeVar

from .gjgameobjectconversiongroups.gjgameobjectconversiongroup import (
    GJGameObjectConversionGroup,
)

# hacky circular import fix
T = TypeVar("T")


@dataclass
class ConversionReport(Generic[T]):
    """
    Options during full level conversion
    """

    converted_triggers: list[T]
    group_conversions: dict[GJGameObjectConversionGroup, list[T]]
    removed_objects: list[T]
    preconversion_object_count: int
