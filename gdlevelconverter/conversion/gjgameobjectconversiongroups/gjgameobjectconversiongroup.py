"""
Defines the id conversion group class for GJGameObjects
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GJGameObjectConversion:
    """
    Defines an object id conversion
    """

    initial_id: int
    resulting_id: int


@dataclass(frozen=True)
class GJGameObjectConversionGroup:
    """
    Defines a conversion group
    """

    name: str
    conversions: List[GJGameObjectConversion]
    show_hitbox_warning: bool = False
    show_visual_warning: bool = False

    def __hash__(self):
        return hash(self.name)
