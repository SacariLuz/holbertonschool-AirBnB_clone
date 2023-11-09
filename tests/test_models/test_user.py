#!/usr/bin/python3
import unittest

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_compare_attrs(self):
        user_dict = self.user.to_dict()
        self.assertNotIn("email", user_dict)
        self.assertNotIn("password", user_dict)
        self.assertNotIn("first_name", user_dict)
        self.assertNotIn("last_name", user_dict)

    def test_is_instantiated(self):
        self.assertIsNotNone(self.user)

    def test_inheric(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_str_magic(self):
        name_class = self.user.__class__.__name__
        id_obj = self.user.id
        dict_obj = self.user.__dict__
        str_magic = f"[{name_class}] ({id_obj}) {dict_obj}"

        self.assertEqual(str(self.user), str_magic)

    def test_exist_attr(self):
        email = "email"
        password = "password"
        first_name = "first_name"
        last_name = "last_name"
        self.user.email = email
        self.user.password = password
        self.user.first_name = first_name
        self.user.last_name = last_name

        self.assertTrue(self.user.email)
        self.assertTrue(self.user.password)
        self.assertTrue(self.user.first_name)
        self.assertTrue(self.user.last_name)

    def test_type_attr(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
