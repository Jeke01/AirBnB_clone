#!/usr/bin/python3
import unittest
from models.place import Place
"""
Unit test module for Place class
"""


class TestPlace(unittest.TestCase):
    ''' Unit tests for Place class '''

    def test_object_instantiation(self):
        ''' Test instantiation of Place class '''
        self.place = Place()

    def test_attributes(self):
        ''' Test attributes of Place class '''
        self.place = Place()
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertFalse(hasattr(self.place, "random_attr"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_save_method(self):
        ''' Test save method of Place class '''
        self.place = Place()
        self.place.save()
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_str_method(self):
        ''' Test __str__ method of Place class '''
        self.place = Place()
        expected_str = "[{}] ({}) {}".format(self.place.__class__.__name__,
                                             str(self.place.id), self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)


if __name__ == '__main__':
    unittest.main()

