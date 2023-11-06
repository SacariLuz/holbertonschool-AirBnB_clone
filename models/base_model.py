#!/usr/bin/python3
"""
Este modulo define la clase BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Representa la clase
    """

    def __init__(self, *args, **kwargs):
        """
        Metodo que inicialize los atributos:
            id, created_at, updated_at
            **kwargs: recibe diccionario
        """
        if bool(kwargs):
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
            storage.new(self)

    def __str__(self):
        """
        Retorna una representación de la instancia
        """

        return f"[{self.__class__.__name__}] ({self.id}) "\
            + str({k: v for k, v in self.__dict__.items() if k != '__class__'})

    def save(self):
        """
        Metodo que actualiza fecha de creación updated_at.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Metodo que devuelve un nuevo diccionario con los atributos de instancia.
        """

        new_dict = self.__dict__.copy()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
