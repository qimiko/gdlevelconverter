"""
Defines test cases for GJLevelString
"""

import unittest
import pathlib
from gdlevelconverter.gjobjects import GJLevelString
from gdlevelconverter.conversion import GJGameObjectConversionGroupsByName
from gdlevelconverter.conversion import ConversionOptions


class TestGJLevelString(unittest.TestCase):
    """
    Test cases for GJLevelString
    """

    TEST_LVL_FILE_NAME = "conv_test1.lvl"

    def test_load_level(self):
        """
        Tests loading level from string
        """

        file_path = pathlib.Path(__file__).parent / self.TEST_LVL_FILE_NAME

        lvl_string = ""
        with open(file_path, "r", encoding="utf8") as lvl:
            lvl_string = lvl.read()

        level = GJLevelString(lvl_string)
        self.assertEqual(len(level.objects), 107)

    def test_save_level(self):
        """
        Tests saving level to string
        """

        file_path = pathlib.Path(__file__).parent / self.TEST_LVL_FILE_NAME

        lvl_string = ""
        with open(file_path, "r", encoding="utf8") as lvl:
            lvl_string = lvl.read()

        level = GJLevelString(lvl_string)
        self.assertEqual(str(level), lvl_string)

    def test_convert_level_to_legacy(self):
        """
        Tests converting level to legacy format
        """

        file_path = pathlib.Path(__file__).parent / self.TEST_LVL_FILE_NAME

        lvl_string = ""
        with open(file_path, "r", encoding="utf8") as lvl:
            lvl_string = lvl.read()

        level = GJLevelString(lvl_string)

        slope_group = GJGameObjectConversionGroupsByName["slopes"]

        report = level.to_legacy_format(
            ConversionOptions(groups=[slope_group], maximum_id=744)
        )

        self.assertEqual(len(report.converted_triggers), 10)
        self.assertEqual(len(report.group_conversions[slope_group]), 1)
