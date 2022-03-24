"""
Defines test cases for GJLevelString
"""
import unittest
from gdlevelconverter.gjobjects import GJLevelString
from gdlevelconverter.conversion import GJGameObjectConversionGroupsByName
from gdlevelconverter.conversion import ConversionOptions


class TestGJLevelString(unittest.TestCase):
    """
    Test cases for GJLevelString
    """

    # i'm so sorry
    TEST_LEVEL_STRING = (
        "kS38,1_0_2_0_3_0_4_-1_6_1000_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_1001_7_1_15_0_18_0_8_1|"
        "1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1009_7_1_15_1_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_1002_5_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_1004_7_1_15_0_18_0_8_1|"
        "1_255_2_250_3_103_4_-1_6_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_2_5_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_3_5_1_7_1_15_0_18_0_8_1|"
        "1_0_2_0_3_0_4_-1_6_4_7_1_15_0_18_0_8_1|"
        "1_255_2_255_3_255_4_-1_6_1003_7_1_15_0_18_0_8_1|"
        "1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1005_5_1_7_1_15_1_18_0_8_1|"
        "1_0_2_255_3_0_11_255_12_255_13_255_4_-1_6_1006_5_1_7_1_15_1_18_0_8_1|,"
        "kA13,0,kA15,0,kA16,1,kA14,,kA6,7,kA7,5,kA17,0,kA18,0,kS39,0,kA2,0,"
        "kA3,0,kA8,0,kA4,0,kA9,0,kA10,0,kA11,0;"
        "1,899,2,15,3,435,36,1,7,127,8,126,9,125,10,2.025,35,1,17,1,23,4;"
        "1,105,2,15,3,405,36,1,7,127,8,126,9,125,10,1.975,35,1,23,1004;"
        "1,503,2,75,3,10,21,4;1,503,2,45,3,10,21,4;1,503,2,15,3,10,21,4;"
        "1,468,2,15,3,1;1,468,2,45,3,1;1,468,2,75,3,1;"
        "1,583,2,67,3,77,4,1,5,1,20,1,21,1;"
        "1,584,2,67,3,84.5,20,1,6,90,21,1;"
        "1,578,2,67,3,99,4,1,5,1,20,1,6,90,21,1;"
        "1,578,2,77,3,109,5,1,20,1,6,180,21,1;"
        "1,584,2,87,3,97.5,4,1,20,1,6,90,21,1;"
        "1,578,2,83,3,91,4,1,5,1,20,1,6,-134,21,1;"
        "1,578,2,95,3,79,20,1,6,-134,21,1;"
        "1,583,2,67,3,77,4,1,5,1,20,2,21,1;"
        "1,584,2,67,3,84.5,20,2,6,90,21,1;"
        "1,578,2,67,3,99,4,1,5,1,20,2,6,90,21,1;"
        "1,578,2,77,3,109,5,1,20,2,6,180,21,1;"
        "1,584,2,87,3,97.5,4,1,20,2,6,90,21,1;"
        "1,578,2,83,3,91,4,1,5,1,20,2,6,-134,21,1;"
        "1,578,2,95,3,79,20,2,6,-134,21,1;"
        "1,507,2,75,3,65,20,2,21,1;"
        "1,583,2,67,3,77,5,1,20,3,21,1;"
        "1,583,2,67,3,77,4,1,5,1,20,3,21,1;"
        "1,584,2,67,3,84.5,20,3,6,90,21,1;"
        "1,578,2,67,3,99,4,1,5,1,20,3,6,90,21,1;"
        "1,578,2,77,3,109,5,1,20,3,6,180,21,1;"
        "1,584,2,87,3,97.5,4,1,20,3,6,90,21,1;"
        "1,578,2,83,3,91,4,1,5,1,20,3,6,-134,21,1;"
        "1,578,2,95,3,79,20,3,6,-134,21,1;"
        "1,507,2,75,3,65,20,3,21,1;"
        "1,583,2,67,3,77,5,1,20,1,21,1;"
        "1,507,2,75,3,65,20,1,21,1;"
        "1,583,2,67,3,77,5,1,20,2,21,1;"
        "1,503,2,195,3,10,21,4;"
        "1,503,2,165,3,10,21,4;"
        "1,503,2,135,3,10,21,4;"
        "1,503,2,105,3,10,21,4;"
        "1,468,2,105,3,1;"
        "1,468,2,135,3,1;"
        "1,468,2,165,3,1;"
        "1,468,2,195,3,1;"
        "1,578,2,129,3,79,20,1,6,-134,21,1;"
        "1,584,2,121,3,97.5,4,1,20,1,6,90,21,1;"
        "1,507,2,131,3,65,4,1,20,1,21,1;"
        "1,899,2,105.5,3,165,20,1,36,1,7,0,8,0,9,0,10,0.225,35,1;"
        "1,578,2,111,3,109,5,1,20,1,6,180,21,1;"
        "1,578,2,101,3,99,4,1,5,1,20,1,6,90,21,1;"
        "1,578,2,117,3,91,4,1,5,1,20,1,6,-134,21,1;"
        "1,507,2,101,3,65,4,1,20,1,21,1;"
        "1,578,2,129,3,79,20,2,6,-134,21,1;"
        "1,584,2,121,3,97.5,4,1,20,2,6,90,21,1;"
        "1,507,2,131,3,65,4,1,20,2,21,1;"
        "1,578,2,111,3,109,5,1,20,2,6,180,21,1;"
        "1,578,2,101,3,99,4,1,5,1,20,2,6,90,21,1;"
        "1,578,2,117,3,91,4,1,5,1,20,2,6,-134,21,1;"
        "1,507,2,101,3,65,4,1,20,2,21,1;"
        "1,578,2,129,3,79,20,3,6,-134,21,1;"
        "1,584,2,121,3,97.5,4,1,20,3,6,90,21,1;"
        "1,507,2,131,3,65,4,1,20,3,21,1;"
        "1,578,2,111,3,109,5,1,20,3,6,180,21,1;"
        "1,578,2,101,3,99,4,1,5,1,20,3,6,90,21,1;"
        "1,578,2,117,3,91,4,1,5,1,20,3,6,-134,21,1;"
        "1,507,2,101,3,65,4,1,20,3,21,1;"
        "1,503,2,285,3,10,21,4;"
        "1,503,2,255,3,10,21,4;"
        "1,503,2,225,3,10,21,4;"
        "1,468,2,225,3,1;"
        "1,468,2,255,3,1;"
        "1,468,2,285,3,1;"
        "1,503,2,315,3,10,21,4;"
        "1,503,2,345,3,10,21,4;"
        "1,503,2,375,3,10,21,4;"
        "1,468,2,315,3,1;"
        "1,468,2,345,3,1;"
        "1,468,2,375,3,1;"
        "1,503,2,435,3,10,21,4;"
        "1,503,2,465,3,10,21,4;"
        "1,503,2,495,3,10,21,4;"
        "1,503,2,405,3,10,21,4;"
        "1,468,2,405,3,1;"
        "1,468,2,435,3,1;"
        "1,468,2,465,3,1;"
        "1,468,2,495,3,1;"
        "1,503,2,525,3,10,21,4;"
        "1,503,2,555,3,10,21,4;"
        "1,503,2,585,3,10,21,4;"
        "1,468,2,525,3,1;"
        "1,468,2,555,3,1;"
        "1,468,2,585,3,1;"
        "1,503,2,615,3,10,21,4;"
        "1,503,2,645,3,10,21,4;"
        "1,503,2,675,3,10,21,4;"
        "1,468,2,615,3,1;"
        "1,468,2,645,3,1;"
        "1,1749,2,675,3,1;"
        "1,899,2,615,3,585,36,1,7,255,8,253,9,250,10,0.1,35,1,17,1,23,4;"
        "1,899,2,645,3,585,36,1,7,127,8,126,9,125,10,1.05,35,1,17,1,23,4;"
        "1,105,2,615,3,615,36,1,7,255,8,253,9,250,10,0.1,35,1,23,1004;"
        "1,105,2,645,3,615,36,1,7,127,8,126,9,125,10,1.025,35,1,23,1004;"
        "1,899,2,615,3,495,36,1,7,57,8,19,9,19,10,0.325,35,1,17,1;"
        "1,899,2,615,3,525,36,1,7,19,8,57,9,23,10,0.325,35,1,17,1,23,2;"
        "1,899,2,615,3,555,36,1,7,21,8,19,9,57,10,0.349998,35,1,17,1,23,3;"
        "1,899,2,675,3,495,36,1,7,21,8,19,9,57,10,0.325,35,1,17,1;"
        "1,899,2,675,3,525,36,1,7,57,8,19,9,19,10,0.275,35,1,17,1,23,2;"
        "1,899,2,675,3,555,36,1,7,19,8,57,9,23,10,0.325,35,1,17,1,23,3;"
    )

    def test_load_level(self):
        """
        Tests loading level from string
        """

        level = GJLevelString(self.TEST_LEVEL_STRING)
        self.assertEqual(len(level.objects), 107)

    def test_save_level(self):
        """
        Tests saving level to string
        """

        level = GJLevelString(self.TEST_LEVEL_STRING)
        self.assertEqual(str(level), self.TEST_LEVEL_STRING)

    def test_convert_level_to_legacy(self):
        """
        Tests converting level to legacy format
        """
        level = GJLevelString(self.TEST_LEVEL_STRING)

        slope_group = GJGameObjectConversionGroupsByName["slopes"]

        report = level.to_legacy_format(
            ConversionOptions(
                groups=[
                    slope_group
                ],
                maximum_id=744
            )
        )

        self.assertEqual(len(report.converted_triggers), 10)
        self.assertEqual(len(report.group_conversions[slope_group]), 1)
