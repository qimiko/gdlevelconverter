"""
Defines GJCustomColorType enum
"""

from enum import IntEnum


class GJCustomColorType(IntEnum):
    """
    Enum used to define custom colors in legacy objects
    """

    COLOR_UNKNOWN = 0
    COLOR_PLAYER1 = 1
    COLOR_PLAYER2 = 2
    COLOR_1 = 3
    COLOR_2 = 4
    COLOR_LBG = 5
    COLOR_3 = 6
    COLOR_4 = 7
    COLOR_3DL = 8
    COLOR_NONE = 9

    @classmethod
    def from_color_channel(cls, channel: int, conv_white: bool = False):
        """
        Returns enum associated with a color channel
        """

        mapping = {
            1: cls.COLOR_1,
            2: cls.COLOR_2,
            3: cls.COLOR_3,
            4: cls.COLOR_4,
            1003: cls.COLOR_3DL,
            1005: cls.COLOR_PLAYER1,
            1006: cls.COLOR_PLAYER2,
            1007: cls.COLOR_LBG,
        }

        if channel in mapping:
            return mapping[channel]

        if conv_white:
            return cls.COLOR_NONE
        else:
            return cls.COLOR_UNKNOWN

    def __str__(self):
        return str(self.value)
