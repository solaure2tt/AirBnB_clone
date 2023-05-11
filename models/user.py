#!/usr/bin/python3

""" This module holds the code for the user class """

from models.base_model import BaseModel


class User(BaseModel):
    """ This is a blue print for all user objects """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
