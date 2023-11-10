#!/usr/bin/python3
"""
Define la clase review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Muestra la reseña de la habitación

    Atributos:

    place_id(str): id del lugar.
    user_id(str): id del usuario.
    text(str): texto de la review.
    """

    place_id = ""
    user_id = ""
    text = ""
