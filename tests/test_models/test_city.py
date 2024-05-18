#!/usr/bin/python3
import unittest
from models.city import City
"""
Unit test module for City class
"""


class TestCity(unittest.TestCase):
    ''' Unit tests for City class '''

    def test_object_instantiation(self):
        ''' Test instantiation of City class '''
        self.city = City()

    def test_attributes(self):
        ''' Test attributes of City class '''
        self.city = City()
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertFalse(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "WonderLand"
        self.city.state_id = "Won67L0nd"
        self.assertEqual(self.city.name, "WonderLand")
        self.assertEqual(self.city.state_id, "Won67L0nd")
        self.assertEqual(self.city.__class__.__name__, "City")

    def test_save_method(self):
        ''' Test save method of City class '''
        self.city = City()
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_str_method(self):
        ''' Test __str__ method of City class '''
        self.city = City()
        expected_str = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                             str(self.city.id), self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()

