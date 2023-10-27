#!/usr/bin/python3
"""
Este modulo define la clase BaseModel
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Esta clase hereda
    """

    def __init__(self):
        """
        Metodo que inicialize los atributos:
            id, created_at, updated_at
            **kwargs: recibe diccionario
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)

            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

            self.__dict__["updated_at"] = datetime.strptime(
                self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Retorna una representación de la instancia
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Metodo que actualiza fecha de creación updated_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Metodo que devuelve un diccionario con los atributos de instancia.
        """

        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.__dict__['created_at'].isoformat()
        my_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return (my_dict)
