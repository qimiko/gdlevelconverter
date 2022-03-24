"""
Defines conversion options class
"""

from dataclasses import dataclass

from ..gjgameobject import GJGameObject
from . import GJGameObjectConversionGroup


@dataclass
class ConversionReport:
    """
    Options during full level conversion
    """
    converted_triggers: list[GJGameObject]
    group_conversions: dict[GJGameObjectConversionGroup, list[GJGameObject]]
    removed_objects: list[GJGameObject]
    preconversion_object_count: int
