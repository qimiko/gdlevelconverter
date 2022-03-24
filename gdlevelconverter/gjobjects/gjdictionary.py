"""
Functions to aid in conversion to and from a Geometry Dash dictionary type
"""

from abc import abstractmethod
from dataclasses import dataclass
from typing import Callable


@dataclass
class ObjectDefinition:
    """
    Defines mappings from string to class object, or back
    """

    key: str
    """
    Object key
    """

    index: str
    """
    Index in response string
    """

    deserialize_as: Callable[[str], any] = None
    """
    Callable to deserialize object into
    """

    serialize_as: Callable[..., str] = None
    """
    Callable to serialize object with
    """


def class_from_string(string: str, splitter: str, definitions: list[ObjectDefinition], cls: object):
    """
    parses the special robtop style array
    - expects string like 1,53,2,65,3,14.3
    - returns dict like {'1': '53', '2': '65', '3': '14.3'}
    """

    split_first_step: list[str] = string.split(splitter)

    for index, _value in enumerate(split_first_step):
        # if odd then we on index
        if index % 2 == 0:

            index_name = split_first_step[index]
            value = split_first_step[index + 1]

            key = next((x for x in definitions if x.index == index_name), None)

            if key:
                if key.deserialize_as:
                    if not value:
                        # needed for proper int conversion
                        setattr(cls, key.key, key.deserialize_as())
                    else:
                        setattr(cls, key.key, key.deserialize_as(value))
                else:
                    setattr(cls, key.key, value)
            else:
                setattr(cls, f"index_{index_name}", value)

    return cls


def as_list(into: Callable[[str], any], splitter: str):
    """
    Used as value in object definition
    Creates a function that converts a string into list with splitter
    """
    def from_str(string: str):
        return [into(x) for x in string.split(splitter) if x]

    return from_str


def from_list(splitter: str):
    """
    Used as value in object definition
    Creates a function that converts a list into string using splitter
    """
    def into_str(obj: list[any]):
        # gd ends lists with splitter from what i can tell
        return splitter.join([str(x) for x in obj]) + splitter

    return into_str


class GJDictionary:
    """
    Base class type for objects that fit the GJDictionary model
    """

    @property
    @abstractmethod
    def _splitter(self) -> str:
        """
        Splitter for use when converting to/from dictionary
        """

    @property
    @abstractmethod
    def _definitions(self) -> list[ObjectDefinition]:
        """
        Defintions for use when converting to/from dictionary
        """

    @classmethod
    def from_str(cls, string: str):
        """
        Creates an instance of cls from string
        """
        instance = cls()

        class_from_string(string, cls._splitter, cls._definitions, instance)

        return instance

    def __init__(self, string: str = None):
        if string:
            class_from_string(string, self._splitter,  self._definitions, self)

    def __info_for_key(self, key: str):
        return next((x for x in self._definitions if x.key == key), None)

    def __map_tuple_key_to_index(self, obj: tuple[str, any]):
        (key, value) = obj

        key_info = self.__info_for_key(key)
        if not key_info:
            # unknown key values
            return (key.removeprefix("index_"), value)

        if key_info.serialize_as:
            return (key_info.index, key_info.serialize_as(value))
        return (key_info.index, value)

    def _get_attributes(self):
        return self.__dict__

    def __str__(self):
        attributes = self._get_attributes()

        mapped_attributes = [
            self.__map_tuple_key_to_index(x) for x in attributes.items()]

        flattened_attributes = [str(x) for y in mapped_attributes for x in y]
        return self._splitter.join(flattened_attributes)

    def __repr__(self):
        return repr(self._get_attributes())

    def __hash__(self):
        return hash(self._get_attributes())

    def __eq__(self, other):
        return self._get_attributes() == other._get_attributes()
