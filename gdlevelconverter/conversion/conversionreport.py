"""
Defines conversion options class
"""

from dataclasses import dataclass
from typing import Generic, TypeVar

from . import GJGameObjectConversionGroup


TYPE = TypeVar("TYPE")

# hacky circular import fix
@dataclass
class ConversionReport(Generic[TYPE]):
    """
    Options during full level conversion
    """
    converted_triggers: list[TYPE]
    group_conversions: dict[GJGameObjectConversionGroup, list[TYPE]]
    removed_objects: list[TYPE]
    preconversion_object_count: int
