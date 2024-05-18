#!/usr/bin/python3
import unittest
from models.state import State
"""
Unit test module for the State class
"""


class TestState(unittest.TestCase):
    ''' Unit tests for the State class '''

    def test_object_instantiation(self):
        ''' Test instantiation of the State class '''
        self.state = State()

    def test_attributes(self):
        ''' Test attributes of the State class '''
        self.state = State()
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertFalse(hasattr(self.state, "random_attr"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertEqual(self.state.name, "")
        self.state.name = "WonderLand"
        self.assertEqual(self.state.name, "WonderLand")
        self.assertEqual(self.state.__class__.__name__, "State")

    def test_save_method(self):
        ''' Test the save method of the State class '''
        self.state = State()
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_str_method(self):
        ''' Test the __str__ method of the State class '''
        self.state = State()
        expected_str = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                             str(self.state.id), self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)


if __name__ == '__main__':
    unittest.main()

