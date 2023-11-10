#!/usr/bin/python3

import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_str_magic(self):
        name_class = self.amenity.__class__.__name__
        id_obj = self.amenity.id
        dict_obj = self.amenity.__dict__
        str_magic = f"[{name_class}] ({id_obj}) {dict_obj}"

        self.assertEqual(str(self.amenity), str_magic)

    def test_is_dict(self):
        self.assertIsInstance(self.amenity.to_dict(), dict)

    def test_compare_attrs(self):
        amenity_attr = self.amenity.to_dict()
        self.assertNotIn("name", amenity_attr)

    def test_name_exists(self):
        amenities = "Amenities"
        self.amenity.name = amenities
        self.assertEqual(self.amenity.name, amenities)

    def test_name_in_attrs(self):
        amenity_attr = self.amenity.to_dict()
        self.assertNotIn("name", amenity_attr)

    def test_type_str(self):
        self.assertEqual(type(self.amenity.name), str)
