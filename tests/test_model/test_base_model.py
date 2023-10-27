#!/usr/bin/python3
"""
Esto es un test para la clase BaseModel
"""

import unittest

from models.base_model import BaseModel
import time

class TestBaseModel(unittest.TestCase):
    """
    Define casos de prueba
    """

    def setUp(self):
        """
        instancia de la clase BaseModel
        """
        self.bm = BaseModel()

    def test_init(self):
        """
        Se realiza prueba que compara los atributos con los tipos de datos
        """
        self.assertIsInstance(self.bm.id, str)

    def test_return(self):
        """
        Esto compara lo que devuelve como None de save()
        """

    def test_compare_attrs(self):
        """
        Verifica que contenga los atributtos
        """
        model_dict = self.bm.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_methods_magic_str(self):
        """
        Esto compara la salida de magic __str__
        """
        bm = BaseModel()
        expected_output = "[{}] ({}) {}".format(
                bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_output)

    def test_update_date(self):
        """
        Actualiza el atributo updated_at
        """
        model = BaseModel()
        original_updated_at = model.updated_at
        time.sleep(1)
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    if __name__ == "__main__":
        unittest.main()
