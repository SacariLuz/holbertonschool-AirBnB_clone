#!/usr/bin/python3
"""
Este módulo define la clase BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Este clase expone BaseModel, la que será nuestra superclase.
    """

    def __init__(self, *args, **kwargs):
        """
        Este método inicializa lo sgte:
            id, created_at, updated_at
        Attr:
            id (str): Genera un id cada vez que se instancia.
            created_ad (str): Genera la hora y fecha cada vez
                    que se instancia un nuevo objeto.
            updated_at (str): Genera y actualiza la hora y fecha,
                    cada vez que se cambia nuestra instancia.
        """
        if bool(kwargs):
            for k, v in kwargs.items():
                if k != '__class__':
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
        """Returns a string in this format:
            BaseModel (uuid4 type id) self.__dict__
        """
        return f"[{self.__class__.__name__}] ({self.id}) "\
            + str({k: v for k, v in self.__dict__.items() if k != '__class__'})

    def save(self):
        """Este método actualiza .updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Este método genera un nuevo diccionario agregando la clave __class__
        Returns:
            new_dict (dict)
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
