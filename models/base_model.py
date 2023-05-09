#!/usr/bin/python3

""" This module holds the class definition of our base model """

import datetime as dt
import uuid
import cmd
import sys
import os
import json

class BaseModel:
    """ This defines the basis of al our objects in this project """
    def __init__(self, *args, **kwargs):
        """ This is the constructor for our class instances """

        if kwargs:
            try:
                self.id = kwargs['id']
                self.created_at = dt.datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = dt.datetime.fromisoformat(kwargs['updated_at'])
            except Exception as e:
                print (e)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()

    def save(self):
        """ This method updates the instance attribut updated_at """
        
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """ This method returns a dict of key-value pairs as per the
        __dict__ builtin of the instance """

        inst_dict = {"__class__": type(self).__name__}

        for key, value in self.__dict__.items():
            if isinstance(value, dt.datetime):
                inst_dict[key] = value.isoformat()
            else:
                inst_dict[key] = value
        return inst_dict

    def __str__(self):
        """ This method returns the string representation of any class
        instance """

        str_rep = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

        return str_rep
