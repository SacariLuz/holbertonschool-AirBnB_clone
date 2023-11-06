#!/usr/bin/python3
""" importamos el archivo file_storage.py de FileStorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
