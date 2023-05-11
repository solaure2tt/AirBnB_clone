#!/usr/bin/python3

""" This module holds the code for a filestorage class """
import os
import json
import sys
import datetime as dt
from models.base_model import BaseModel


class FileStorage:
    """ This isclass serializes instance to a JSON file and vice versa """

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ This method writees to the __object dict
        Args:
            obj: list of objects
        """

        if obj is not None:
            try:
                key = type(obj).__name__ + '.' + obj.id
                self.__objects[key] = obj
            except Exception as e:
                print(e)

    def save(self):
        """ This method serializes __objects to __file_path """

        with open(self.__file_path, 'w') as file:
            if self.__objects is None:
                file.write("[]")
            else:
                ins = {}
                all_objs = self.all()
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    my_model_json = {"__class__": type(obj).__name__}
                    for key, value in obj.__dict__.items():
                        if isinstance(value, dt.datetime):
                            my_model_json[key] = value.isoformat()
                        else:
                            my_model_json[key] = value
                    ins[obj_id] = my_model_json
                file.write(json.dumps(ins, default=str))

    def reload(self):
        """ This method deserializes a JSON obeject to class object """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                re = file.read()
                listDict = json.loads(re)
                obj = {}
                for di in listDict:
                    obj[di] = listDict[di]
                if obj is not None:
                    for k in obj.keys():
                        ob = obj[k]
                        key = ob['__class__'] + '.' + ob['id']
                        self.__objects[key] = BaseModel(**ob)
