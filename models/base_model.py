#!/usr/rin/python3
"""Este modulo define la clase BaseModel"""


import uuid
import datetime


class BaseModel:

    """Esta clase represent BaseModel"""

    def __init__(self):
        """metodo que inicialize"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        devuelve una representacion de nuestra instancia
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """metodo que actualiza la fecha de creación updated_at."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        metodo que devuelve un diccionario

        Returns:
        dict:devuelve un diccionario con los atributos de instancia.
        """
        ttributes = self.__dict__.copy()
        attributes["__class__"] = self.__class__.__name__
        attributes["created_at"] = self.created_at.isoformat()
        attributes["updated_at"] = self.updated_at.isoformat()
        return attributes
