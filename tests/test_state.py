#!/usr/bin/python3

import unittest

from models.state import State
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_is_instantiated(self):
        self.assertIsNotNone(self.state)

    def test_inheric(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_str_magic(self):
        name_class = self.state.__class__.__name__
        id_obj = self.state.id
        dict_obj = self.state.__dict__
        str_magic = f"[{name_class}] ({id_obj}) {dict_obj}"

        self.assertEqual(str(self.state), str_magic)

    def test_compare_attrs(self):
        state_attr = self.state.to_dict()
        self.assertNotIn("name", state_attr)

    def test_exist_attr(self):
        name = "name"
        self.state.name = name
        self.assertTrue(self.state.name)

    def test_type_attr(self):
        self.assertIsInstance(self.state.name, str)
