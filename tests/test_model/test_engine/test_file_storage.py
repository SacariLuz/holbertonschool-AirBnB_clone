#!/usr/bin/python3

import unittest
from datetime import datetime
from time import sleep
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path


class TestStorage(unittest.TestCase):
    # def test_file_path(self):
    #     self.assertIsNone(FileStorage.__file_path)

    def test_file_path1(self):
        self.assertTrue(path.exists(FileStorage._FileStorage__file_path))

    def test_update_now(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        original_created_at = model.created_at
        sleep(1)
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)
        self.assertTrue(original_created_at, model.created_at)
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_save(self):
        model = BaseModel()
        self.assertIsNone(model.save())

    def test_update_type(self):
        model = BaseModel()
        self.assertTrue(type(model.updated_at) == datetime)
