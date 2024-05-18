#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""
Unit test module for Amenity class
"""


class TestAmenity(unittest.TestCase):
    ''' Unit tests for Amenity class '''

    def test_object_instantiation(self):
        ''' Test instantiation of Amenity class '''
        self.amenity = Amenity()

    def test_attributes(self):
        ''' Test attributes of Amenity class '''
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")

    def test_save_method(self):
        ''' Test save method of Amenity class '''
        self.amenity = Amenity()
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_str_method(self):
        ''' Test __str__ method of Amenity class '''
        self.amenity = Amenity()
        expected_str = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                             str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)


if __name__ == '__main__':
    unittest.main()

