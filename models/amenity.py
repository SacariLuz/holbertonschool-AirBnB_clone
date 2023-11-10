#!/usr/bin/python3
"""
Define la clase amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Enseña comodidades de la habitacion

    Atributos:
    name (str): nombres de las comodidades
    """

    name = ""
