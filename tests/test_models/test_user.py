#!/usr/bin/python3

import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' Unit tests for the User class '''

    @classmethod
    def setUpClass(cls):
        ''' Set up a User instance for testing '''
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Holberton"
        cls.my_user.email = "airbnb@holbertonshool.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        ''' Clean up the User instance after tests '''
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        ''' Test if User is a subclass of BaseModel '''
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel))

    def test_checking_for_functions(self):
        ''' Test if User class has a docstring '''
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        ''' Test if User instance has specific attributes '''
        self.assertIn('email', self.my_user.__dict__)
        self.assertIn('id', self.my_user.__dict__)
        self.assertIn('created_at', self.my_user.__dict__)
        self.assertIn('updated_at', self.my_user.__dict__)
        self.assertIn('password', self.my_user.__dict__)
        self.assertIn('first_name', self.my_user.__dict__)
        self.assertIn('last_name', self.my_user.__dict__)

    def test_attributes_are_strings(self):
        ''' Test if User attributes are of type string '''
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)

    def test_save(self):
        ''' Test the save method of the User class '''
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        ''' Test the to_dict method of the User class '''
        self.assertIn('to_dict', dir(self.my_user))


if __name__ == "__main__":
    unittest.main()

