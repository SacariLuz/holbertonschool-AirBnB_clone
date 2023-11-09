#!/usr/bin/python3
"""Creamos la clase user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Esta clase contiene los atributos del user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
