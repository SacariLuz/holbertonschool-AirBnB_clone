#!/usr/rin/python3
"""Este modulo define la clase BaseModel"""


import uuid
import datetime


class BaseModel:

    """Esta clase represent BaseModel"""

    def __init__(self):
        """
        Este medoto inicialize:
            id, created_at, update_at
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Este metodo regresa a una representacion de nuestra instancia
        Return:
            str: Representa instancia
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Este metodo actualiza la fecha de creación updated_at."""
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        Este metodo regresa un diccionado
        Returns:
            dict:devuelve un diccionario con los atributos de instancia.
        """
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
