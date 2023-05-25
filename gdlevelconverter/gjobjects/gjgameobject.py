"""
GJGameObject class definition
"""

from typing import Optional, List

from ..conversion import GJGameObjectConversionGroup
from ..conversion import TriggerObjectColorConversions
from .enums import GJCustomColorType
from . import gjdictionary


class GJGameObject(gjdictionary.GJDictionary):
    """
    Deserialized representation of Geometry Dash object
    """

    UNIFIED_COLOR_TRIGGER_ID = 899

    _definitions = [
        gjdictionary.ObjectDefinition(
            key="object_id", index="1", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="x_position", index="2", deserialize_as=float),
        gjdictionary.ObjectDefinition(key="y_position", index="3", deserialize_as=float),
        gjdictionary.ObjectDefinition(
            key="legacy_object_color", index="19"),
        gjdictionary.ObjectDefinition(
            key="line_color", index="21", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="object_color", index="22", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="color_trigger_target", index="23", deserialize_as=int),
    ]

    _splitter = ","

    object_id: int

    x_position: float
    y_position: float

    legacy_object_color: Optional[GJCustomColorType]
    line_color: Optional[int]
    object_color: Optional[int]

    color_trigger_target: Optional[int]

    def to_legacy_color(self) -> bool:
        """
        Converts an object to use the legacy 1.9 color format, if applicable
        Returns True if conversion was performed
        """
        if hasattr(self, "object_color"):
            self.legacy_object_color = GJCustomColorType.from_color_channel(
                self.object_color)

            del self.object_color
            if hasattr(self, "line_color"):
                del self.line_color
            return True

        if hasattr(self, "line_color"):
            # object color is usually used to describe the object color
            # line color is used as a fallback
            self.legacy_object_color = GJCustomColorType.from_color_channel(
                self.line_color)

            del self.line_color
            return True

        return False

    def remap_to_legacy_id_by_groups(
        self,
        groups: List[GJGameObjectConversionGroup]
    ) -> Optional[GJGameObjectConversionGroup]:
        """
        Remaps the object's id based on the ids defined in groups
        Returns the group the object fit, if any
        """
        conversions_only = {x: y for y in groups
                            for x in y.conversions if x.initial_id == self.object_id}

        # as of right now multiple conversions aren't supported
        # if they happen then you're probably doing the wrong thing

        if not conversions_only:
            return None

        (conversion, group) = next(iter(conversions_only.items()))

        self.object_id = conversion.resulting_id

        return group

    def remap_to_legacy_id_by_target(self):
        """
        Remaps the object's id based on color trigger group
        Returns True if remapping was performed
        """

        if not self.object_id == self.UNIFIED_COLOR_TRIGGER_ID:
            return False

        if not hasattr(self, "color_trigger_target"):
            # if not defined, 1 is the default target
            self.color_trigger_target = 1

        conversion = next(
            (x for x in TriggerObjectColorConversions
             if x.color_channel == self.color_trigger_target), None)

        if not conversion:
            return False

        self.object_id = conversion.result_id

        del self.color_trigger_target

        return True
