"""
Defines GJLevelSettingsObject test cases
"""


import unittest

from gdlevelconverter.gjobjects.gjlevelsettingsobject import GJLevelSettingsObject


class TestGJLevelSettingsObject(unittest.TestCase):
    """
    Test cases for GJLevelSettingsObject
    """

    TEST_LEVEL_HEADER = (
        "kS38,1_0_2_0_3_0_4_-1_6_1000_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_1001_7_1_15_0_18_0_8_1|"
        "1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1009_7_1_15_1_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_1002_5_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_1004_7_1_15_0_18_0_8_1|1_255_2_250_3_103_4_-1_6_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_2_5_1_7_1_15_0_18_0_8_1|1_0_2_0_3_0_4_-1_6_3_5_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_4_7_1_15_0_18_0_8_1|1_255_2_255_3_255_4_-1_6_1003_7_1_15_0_18_0_8_1|"
        "1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1005_5_1_7_1_15_1_18_0_8_1|"
        "1_0_2_255_3_0_11_255_12_255_13_255_4_-1_6_1006_5_1_7_1_15_1_18_0_8_1|,"
        "kA13,0,kA15,0,kA16,1,kA14,,kA6,7,kA7,5,kA17,0,kA18,0,kS39,0,kA2,0,kA3,0,"
        "kA8,0,kA4,0,kA9,0,kA10,0,kA11,0")

    def test_deserialization(self):
        """
        Ensure level settings deserialize properly
        """
        settings = GJLevelSettingsObject(self.TEST_LEVEL_HEADER)

        self.assertEqual(len(settings.color_list), 12)

    def test_legacy_conversion(self):
        """
        Test conversion into a correct 1.9 level form
        """

        settings = GJLevelSettingsObject(self.TEST_LEVEL_HEADER)

        settings.to_legacy_format()

        self.assertEqual((settings.color_ground.red, settings.color_ground.green,
                         settings.color_ground.blue), (0, 0, 0))
        self.assertEqual((settings.color_1.red, settings.color_1.green,
                         settings.color_1.blue), (255, 250, 103))
