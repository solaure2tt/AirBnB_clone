#!/usr/bin/python3
""" This module holds the code for review objects """


from models.base_model import BaseModel


class Review(BaseModel):
    """ This is a blueprint for Review objects """

    place_id = ""
    user_id = ""
    text = ""
