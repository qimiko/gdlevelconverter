"""
Defines test cases for GJGameLevel
"""

import unittest
import pathlib
from gdlevelconverter.gjobjects import GJGameLevel


class TestGJGameLevel(unittest.TestCase):
    """
    Test cases for GJGameLevel
    """

    TEST_GMD_FILE_NAME = "maki_roll.gmd"

    def test_from_gmd(self):
        """
        Test loading from basic gmd file
        """

        file_path = pathlib.Path(__file__).parent / self.TEST_GMD_FILE_NAME

        gmd_string = ""
        with open(file_path, "r", encoding="utf8") as gmd:
            gmd_string = gmd.read()

        level = GJGameLevel.from_gmd(gmd_string)
        self.assertEqual(level.name, "maki roll")
        self.assertEqual(len(level.level_string.objects), 19999)

    def test_to_gmd(self):
        """
        Test saving level to gmd file
        """

        file_path = pathlib.Path(__file__).parent / self.TEST_GMD_FILE_NAME

        gmd_string = ""
        with open(file_path, "r", encoding="utf8") as gmd:
            gmd_string = gmd.read()

        level = GJGameLevel.from_gmd(gmd_string)

        resulting_gmd = level.to_gmd()

        self.assertTrue(
            resulting_gmd.startswith("<d><k>kCEK</k><i>4</i><k>k2</k><s>maki roll</s>")
        )
