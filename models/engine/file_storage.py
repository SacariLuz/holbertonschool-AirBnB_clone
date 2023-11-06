#!/usr/bin/python3
"""Define una clase FileStorage"""

import json
from os import path
import datetime


class FileStorage:
    """Representa la clase FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Devuelve contenido a __objects
        cuando se llama a una instancia de la clase"""
        return self.__objects

    def new(self, obj):
        """Este metodo toma obj como argumento y construye __objects
        diccionario usando el nombre de la clase y el id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """El metodo guarda archivo __file_path
        y json.dumps lo utiliza para escribir un diccionario a __objects
        en el archivo en formato json
        """
        data = {}

        odict = self.__objects
        data = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """
        Metodo que lee un archivo en formato .json, que se guardo
        previamente con .save().
        se convertirá a objetos de python (dict) y se utiliza
        para recuperar las instancias de clase BaseModel que se crearon
        anteriormente, estan istancias serán almacendas en .__objects
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objs = json.load(f)
            for k, v in objs.items():
                from models.base_model import BaseModel
                bs = BaseModel(**v)
                FileStorage.__objects[k] = bs

    def attributes(self):
        """
        Devuelve los atributos válidos y sus tipos para el nombre de
        clase
        """
        attributes = {
            "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
            "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                }

        }

        return attributes
