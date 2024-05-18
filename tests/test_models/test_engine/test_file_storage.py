#!/usr/bin/python3
"""
Unit Test Module for FileStorage
"""
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    ''' Unit tests for FileStorage class '''

    def test_instantiation(self):
        ''' Check if the instance is of class FileStorage '''
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_access(self):
        ''' Test read-write access permissions '''
        rd = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(rd)
        wr = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(wr)
        ex = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertFalse(ex)

    def test_new(self):
        ''' Test the new method (saves a new object into the dictionary) '''
        m_storage = FileStorage()
        instances_dict = m_storage.all()
        user = User()
        user.id = 999999
        user.name = "Aman"
        m_storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(instances_dict[key])

    def test_reload(self):
        ''' Test the reload method (reloads objects from a JSON file) '''
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIsNone(a_storage.reload())

    def test_func_docs(self):
        ''' Test that all functions have docstrings '''
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_save(self):
        ''' Test the save method '''
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        initial_dict = obj.all()
        obj.save()
        obj.reload()
        reloaded_dict = obj.all()
        initial_key = list(initial_dict.keys())[0]
        reloaded_key = list(reloaded_dict.keys())[0]
        self.assertEqual(initial_dict[initial_key].to_dict(), reloaded_dict[reloaded_key].to_dict())


if __name__ == '__main__':
    unittest.main()

