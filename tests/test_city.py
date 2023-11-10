#!/usr/bin/python3

import unittest

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_is_instantiated(self):
        self.assertIsNotNone(self.city)

    def test_inheric(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_str_magic(self):
        name_class = self.city.__class__.__name__
        id_obj = self.city.id
        dict_obj = self.city.__dict__
        str_magic = f"[{name_class}] ({id_obj}) {dict_obj}"

        self.assertEqual(str(self.city), str_magic)

    def test_compare_attrs(self):
        city_attr = self.city.to_dict()
        self.assertNotIn("state_id", city_attr)
        self.assertNotIn("name", city_attr)

    def test_exist_attr(self):
        state_id = "my_id"
        name = "name"
        self.city.state_id = state_id
        self.city.name = name
        self.assertTrue(self.city.state_id)
        self.assertTrue(self.city.name)

    def test_type_attr(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
