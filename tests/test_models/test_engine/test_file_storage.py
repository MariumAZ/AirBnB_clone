#!usr/bin/env python3

from unittest import TestCase
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(TestCase):
    def test_all(self):
        """
        tests all method 
        """
        storage = FileStorage()
        new_dict = storage.all()
        self.assertIsInstance(new_dict, dict)
        self.assertEqual(new_dict, FileStorage.__objects)
        
    def test__file_path(self):
        self.assertIsInstance(FileStorage.__file_path, str)

    def test__objects(self):
        self.assertIsInstance(FileStorage.__objects, dict)

    def test_new(self): 
        """
        tests that new adds an object to    
        """
        from models import base_model
        storage = FileStorage()
        dict = storage.__objects.copy()
        new_instance = base_model.BaseModel()
        storage.new(new_instance)
        new_key = str(new_instance.__class__.__name__) + '.' +  new_instance.id
        dict[new_key] = new_instance
        self.assertEqual(dict, storage.all())

        



        








            
