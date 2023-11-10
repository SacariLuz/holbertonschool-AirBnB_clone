#!/usr/bin/python3
"""
Define la clase state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Define nombre del estado de la ciudad

    Atributos:
        name(str): estado de la ciudad
    """

    name = ""
