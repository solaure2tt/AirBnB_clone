#!/usr/bin/python3

""" This module holds the code for a filestorage class """

class FileStorage:
    """ This isclass serializes instance to a JSON file and vice versa """

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects """

        return FileStorage.__objects

    def new(self):
        """ This method writees to the __object dict """

        key = type(self).__name__ + '.' + self.id

        FileStorage.__objects[key] = self.__str__()

    def save(self):
        """ This method serializes __objects to __file_path """

        with open(__file_path, 'a') as file:
            file.write(json.dumps(FileStorage__objects))

    def reload(self):
        """ This method deserializes a JSON obeject to class object """

        with open(__file_path, 'r') as file:
            self.__objects = json.loads(file.read())
