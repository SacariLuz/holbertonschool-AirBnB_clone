#!/usr/bin/python3

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstatiation(unittest.TestCase):
    """
    Testing the instatiation
    """

    def test_FileStorage_instatiation_no_arg(self):
        # Creando test sin argumentos
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instatiation_with_arg(self):
        # Creando test con argunmentos
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_initializes(self):
        # Test del storage
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        self.assertEqual(dict, type(models.storage.all()))
    
    def test_new(self):
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        with self.assetRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == '__main__':
    unittest.main()
