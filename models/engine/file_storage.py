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
        return FileStorage.__objects

    def new(self, obj):
        """Este metodo toma obj como argumento y construye __objects
        diccionario usando el nombre de la clase y el id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """El metodo guarda archivo un diccionario a __objects
        en el archivo en formato json
        """
         new_dict = {}

        for k, obj in FileStorage.__objects.items():
            new_dict[k] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

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
                },

        }

        return attributes
