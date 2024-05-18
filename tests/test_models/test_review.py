#!/usr/bin/python3
import unittest
from models.review import Review
"""
Unit test module for the Review class
"""


class TestReview(unittest.TestCase):
    ''' Unit tests for the Review class '''

    def test_object_instantiation(self):
        ''' Test instantiation of the Review class '''
        self.review = Review()

    def test_attributes(self):
        ''' Test attributes of the Review class '''
        self.review = Review()
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertFalse(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def test_save_method(self):
        ''' Test the save method of the Review class '''
        self.review = Review()
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_str_method(self):
        ''' Test the __str__ method of the Review class '''
        self.review = Review()
        expected_str = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                             str(self.review.id), self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)


if __name__ == '__main__':
    unittest.main()

