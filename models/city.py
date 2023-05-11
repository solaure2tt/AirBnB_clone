#!/usr/bin/python3
""" This module holds the code for city objects """


from models.base_model import BaseModel


class City(BaseModel):
    """ This class is a bluprint for all city objects """

    state_id = ""
    name = ""
