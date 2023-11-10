#!/usr/bin/python3

import unittest

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_is_instantiated(self):
        self.assertIsNotNone(self.review)

    def test_compare_attrs(self):
        review_attr = self.review.to_dict()
        self.assertNotIn("place_id", review_attr)
        self.assertNotIn("user_id", review_attr)
        self.assertNotIn("text", review_attr)

    def test_inheric(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_str_magic(self):
        name_class = self.review.__class__.__name__
        id_obj = self.review.id
        dict_obj = self.review.__dict__
        str_magic = f"[{name_class}] ({id_obj}) {dict_obj}"

        self.assertEqual(str(self.review), str_magic)

    def test_exist_attr(self):
        place_id = "my_id"
        text = "text"
        user_id = "user_id"
        self.review.place_id = place_id
        self.review.text = text
        self.review.user_id = user_id
        self.assertTrue(self.review.place_id)
        self.assertTrue(self.review.text)
        self.assertTrue(self.review.user_id)

    def test_type_attr(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.user_id, str)
