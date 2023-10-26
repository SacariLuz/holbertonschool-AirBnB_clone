#!/usr/bin/python3
"""Este modulo define la clase BaseModel"""


import uuid
from detetime
import datetime
import models


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
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """metodo que actualiza la fecha de creación updated_at."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        metodo que devuelve un diccionario

        Returns:
        dict:devuelve un diccionario con los atributos de instancia.
        """

        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.__dict__['created_at'].isoformat()
        my_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return (my_dict)
