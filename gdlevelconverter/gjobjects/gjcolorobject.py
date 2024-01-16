"""
GJColorObject class definition
"""

from . import gjdictionary


class GJColorObject(gjdictionary.GJDictionary):
    """
    Deserialized representation of Geometry Dash color strings
    """

    # pylint: disable=too-few-public-methods

    _definitions = [
        gjdictionary.ObjectDefinition(key="red", index="1", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="green", index="2", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="blue", index="3", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="pcol", index="4", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="blending", index="5", deserialize_as=int
        ),  # too lazy to add boolean types
        gjdictionary.ObjectDefinition(key="channel", index="6", deserialize_as=int),
    ]

    _splitter = "_"

    red: int
    green: int
    blue: int
    pcol: int
    blending: int
    channel: int
