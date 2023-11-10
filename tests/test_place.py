#!/usr/bin/python3

import unittest

from models.place import Place
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_compare_attrs(self):
        place_attr = self.place.to_dict()
        self.assertNotIn("city_id", place_attr)
        self.assertNotIn("user_id", place_attr)
        self.assertNotIn("name", place_attr)
        self.assertNotIn("description", place_attr)
        self.assertNotIn("number_rooms", place_attr)
        self.assertNotIn("number_bathrooms", place_attr)
        self.assertNotIn("max_guest", place_attr)
        self.assertNotIn("price_by_night", place_attr)
        self.assertNotIn("latitude", place_attr)
        self.assertNotIn("longitude", place_attr)
        self.assertNotIn("amenity_ids", place_attr)

    def test_is_instantiated(self):
        self.assertIsNotNone(self.place)

    def test_inheric(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_str_magic(self):
        name_class = self.place.__class__.__name__
        id_obj = self.place.id
        dict_obj = self.place.__dict__
        str_magic = f"[{name_class}] ({id_obj}) {dict_obj}"

        self.assertEqual(str(self.place), str_magic)

    def test_exist_attr(self):
        city_id = "my_id"
        name = "name"
        self.place.city_id = city_id
        self.place.name = name
        self.assertTrue(self.place.city_id)
        self.assertTrue(self.place.name)

    def test_type_attr(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.name, str)
