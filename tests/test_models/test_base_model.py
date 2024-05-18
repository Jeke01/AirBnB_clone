#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
Unit test module for BaseModel class
"""


class TestBaseModel(unittest.TestCase):
    ''' Unit tests for BaseModel class '''

    def test_object_instantiation(self):
        ''' Test instantiation of BaseModel class '''
        self.basemodel = BaseModel()

    def test_checking_for_functions(self):
        ''' Test the presence of docstrings for BaseModel methods '''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        ''' Test attributes of BaseModel class '''
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "random_attr"))
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.basemodel.name = "Alice"
        self.basemodel.age = "44"
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemodel, "name"))
        delattr(self.basemodel, "age")
        self.assertFalse(hasattr(self.basemodel, "age"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def test_save_method(self):
        ''' Test save method of BaseModel class '''
        self.basemodel = BaseModel()
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def test_str_method(self):
        ''' Test __str__ method of BaseModel class '''
        self.basemodel = BaseModel()
        expected_str = "[{}] ({}) {}".format(self.basemodel.__class__.__name__,
                                             str(self.basemodel.id),
                                             self.basemodel.__dict__)
        self.assertEqual(str(self.basemodel), expected_str)

    def test_to_dict(self):
        ''' Test to_dict method of BaseModel class '''
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()

