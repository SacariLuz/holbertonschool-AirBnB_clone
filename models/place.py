#!/usr/bin/python3
"""
Define la clase place
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """ Define nombre del lugar

    Atributos:
        city_id(str): id de ciudad.
        user_id(str): id del usuario.
        name(str): nombredel lugar.
        description(str): descripción del lugar.
        number_rooms(int): numero de cuartos.
        number_bathrooms(int): numero de baños.
        max_guest(int): numero de huéspedes.
        price_by_night(int): precio por noche.
        latitude (float): latitud del lugar.
        longitude (float): longitud del lugar.
        amenity_ids (list): lista de comodidades.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
