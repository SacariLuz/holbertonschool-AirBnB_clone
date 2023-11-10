#!/usr/bin/python3
"""
Define la clase city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Define nombre de la ciudad

    Atributos:
        name(str):nombre de la ciudad
        state_id (str): id del estado
    """

    state_id = ""
    name = ""
