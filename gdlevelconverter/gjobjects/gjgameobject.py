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
        gjdictionary.ObjectDefinition(key="object_id", index="1", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="x_position", index="2", deserialize_as=float
        ),
        gjdictionary.ObjectDefinition(
            key="y_position", index="3", deserialize_as=float
        ),
        gjdictionary.ObjectDefinition(key="flip_x", index="4", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="flip_y", index="5", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="rotation", index="6", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="color_trigger_red", index="7", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_green", index="8", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_blue", index="9", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_duration", index="10", deserialize_as=float
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_touch", index="11", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="coin_id", index="12", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="preview_enabled", index="13", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_tint_ground", index="14", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_copy_pcol1", index="15", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_copy_pcol2", index="16", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_blend", index="17", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="legacy_object_color", index="19"),
        gjdictionary.ObjectDefinition(
            key="editor_group", index="20", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="line_color", index="21", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="object_color", index="22", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(
            key="color_trigger_target", index="23", deserialize_as=int
        ),
    ]

    _splitter = ","

    object_id: int

    x_position: float
    y_position: float

    flip_x: Optional[int]
    flip_y: Optional[int]
    rotation: Optional[int]
    color_trigger_red: Optional[int]
    color_trigger_green: Optional[int]
    color_trigger_blue: Optional[int]
    color_trigger_duration: Optional[float]
    color_trigger_touch: Optional[int]
    coin_id: Optional[int]
    preview_enabled: Optional[int]
    color_trigger_tint_ground: Optional[int]
    color_trigger_copy_pcol1: Optional[int]
    color_trigger_copy_pcol2: Optional[int]
    color_trigger_blend: Optional[int]
    legacy_object_color: Optional[GJCustomColorType]
    editor_group: Optional[int]
    line_color: Optional[int]
    object_color: Optional[int]

    color_trigger_target: Optional[int]

    def to_legacy_color(self, conv_white: bool = False) -> bool:
        """
        Converts an object to use the legacy 1.9 color format, if applicable
        Returns True if conversion was performed
        """
        if hasattr(self, "object_color"):
            self.legacy_object_color = GJCustomColorType.from_color_channel(
                self.object_color, conv_white
            )

            del self.object_color
            if hasattr(self, "line_color"):
                del self.line_color
            return True

        if hasattr(self, "line_color"):
            # object color is usually used to describe the object color
            # line color is used as a fallback
            self.legacy_object_color = GJCustomColorType.from_color_channel(
                self.line_color, conv_white
            )

            del self.line_color
            return True

        return False

    def remap_to_legacy_id_by_groups(
        self, groups: List[GJGameObjectConversionGroup]
    ) -> Optional[GJGameObjectConversionGroup]:
        """
        Remaps the object's id based on the ids defined in groups
        Returns the group the object fit, if any
        """
        conversions_only = {
            x: y
            for y in groups
            for x in y.conversions
            if x.initial_id == self.object_id
        }

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
            (
                x
                for x in TriggerObjectColorConversions
                if x.color_channel == self.color_trigger_target
            ),
            None,
        )

        if not conversion:
            return False

        self.object_id = conversion.result_id

        del self.color_trigger_target

        return True
