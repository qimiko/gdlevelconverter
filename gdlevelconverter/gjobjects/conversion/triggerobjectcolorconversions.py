"""
Defines conversions for color triggers to their legacy triggers
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TriggerObjectColorConversion():
    """
    Defines a conversion between color channel and trigger id
    """
    color_channel: int
    result_id: int


TriggerObjectColorConversions: list[TriggerObjectColorConversion] = [
    TriggerObjectColorConversion(1, 221),
    TriggerObjectColorConversion(2, 717),
    TriggerObjectColorConversion(3, 718),
    TriggerObjectColorConversion(4, 743),
    TriggerObjectColorConversion(1000, 29),
    TriggerObjectColorConversion(1001, 30),
    TriggerObjectColorConversion(1002, 104),
    TriggerObjectColorConversion(1003, 744),
    TriggerObjectColorConversion(1004, 105),
]
