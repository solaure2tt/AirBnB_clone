#!/usr/bin/python3
""" This module holds the code for all place objects """


from models.base_model import BaseModel

class Place(BaseModel):
    """ This is a blueprint for all place objects """

    city_id = ""
    user_id = ""
    name = ""
    ddescription = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
