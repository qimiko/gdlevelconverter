"""
Defines test cases for GJGameObject
"""

import unittest
from gdlevelconverter import GJGameObjectConversionGroupsByName
from gdlevelconverter.gjobjects import GJGameObject


class TestGJGameObject(unittest.TestCase):
    """
    Test cases for GJGameObject
    """

    TEST_LINE_COLOR_OBJECT = "1,508,2,1374.54,3,170.979,5,1,20,1,6,22,21,1"

    TEST_COLOR_OBJECT = "1,216,2,13892.3,3,343.163,5,1,22,1"

    TEST_TRIGGER_OBJECT = "1,899,2,15,3,435,36,1,7,127,8,126,9,125,10,2.025,35,1,17,1,23,4"

    TEST_SLOPE_OBJECT = "1,1749,2,12,3,54"

    def test_deserialization(self):
        """
        Ensure object deserializes properly
        """
        game_obj = GJGameObject(self.TEST_TRIGGER_OBJECT)

        self.assertEqual(game_obj.object_id, 899)

    def test_to_legacy_color(self):
        """
        Test color conversion to 1.9 form
        """
        game_obj = GJGameObject(self.TEST_COLOR_OBJECT)

        game_obj.to_legacy_color()

        self.assertEqual(game_obj.legacy_object_color, 3)

    def test_to_legacy_color_line(self):
        """
        Test color conversion to 1.9 form using a base color object
        """
        game_obj = GJGameObject(self.TEST_LINE_COLOR_OBJECT)

        game_obj.to_legacy_color()

        self.assertEqual(game_obj.legacy_object_color, 3)

    def test_to_legacy_color_trigger(self):
        """
        Test object conversion to legacy color trigger from 2.0 trigger
        """
        game_obj = GJGameObject(self.TEST_TRIGGER_OBJECT)

        game_obj.remap_to_legacy_id_by_target()

        self.assertEqual(game_obj.object_id, 743)

    def test_to_legacy_object_conversion(self):
        """
        Test slope object conversion to legacy object
        """

        game_obj = GJGameObject(self.TEST_SLOPE_OBJECT)

        game_obj.remap_to_legacy_id_by_groups(
            [GJGameObjectConversionGroupsByName["slopes"]]
        )

        self.assertEqual(game_obj.object_id, 315)
