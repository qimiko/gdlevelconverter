"""
Defines GJDictionary test cases using a test object
"""

import unittest

from gdlevelconverter.gjobjects import gjdictionary


class GJTestObject(gjdictionary.GJDictionary):
    """
    Deserialized representation of Geometry Dash object
    """
    _definitions = [
        gjdictionary.ObjectDefinition(
            key="object_id", index="1", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="title", index="2"),
        gjdictionary.ObjectDefinition(
            key="names", index="3",
            deserialize_as=gjdictionary.as_list(str, ";"),
            serialize_as=gjdictionary.from_list(";"))
    ]

    _splitter = ","

    object_id: int

    title: str

    names: list[str]


class TestGJDictionary(unittest.TestCase):
    """
    Test cases for GJDictionary
    """

    TEST_STRING = "1,3,2,test,3,a;b;c;d;"
    TEST_ID = 3
    TEST_TITLE = "test"
    TEST_NAMES = ["a", "b", "c", "d"]

    TEST_UNKNOWN_STRING = "k23,unknown"

    TEST_UNKNOWN_INDEX = "k23"
    TEST_UNKNOWN_VALUE = "unknown"

    def test_deserialization(self):
        """
        Tests object generation from string
        """
        obj = GJTestObject(self.TEST_STRING)
        self.assertEqual(obj.title, self.TEST_TITLE)

    def test_numeric_deserialization(self):
        """
        Tests int conversion from string
        """
        obj = GJTestObject(self.TEST_STRING)
        self.assertEqual(obj.object_id, self.TEST_ID)

    def test_list_deserialization(self):
        """
        Tests list conversion from string
        """
        obj = GJTestObject(self.TEST_STRING)
        self.assertEqual(obj.names, self.TEST_NAMES)

    def test_serialization(self):
        """
        Tests object conversion to string by converting to string and back
        """

        obj = GJTestObject(self.TEST_STRING)

        self.assertEqual(str(obj), self.TEST_STRING)

    def test_unknown_deserialization(self):
        """
        Tests unknown field conversion from string
        """
        obj = GJTestObject(self.TEST_UNKNOWN_STRING)

        self.assertEqual(
            getattr(obj, f"index_{self.TEST_UNKNOWN_INDEX}"), self.TEST_UNKNOWN_VALUE)

    def test_unknown_serialization(self):
        """
        Tests unknown field conversion into string
        """
        obj = GJTestObject(self.TEST_UNKNOWN_STRING)

        self.assertEqual(str(obj), self.TEST_UNKNOWN_STRING)
