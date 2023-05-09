#!/usr/bin/python3
"""File to test the module base_model"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel"""

    def test_uniqueUUID(self):
        """Test if the id is unique and is a string"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertIsInstance(my_model1.id, str)
        self.assertIsInstance(my_model2.id, str)
        self.assertNotEqual(my_model1.id, my_model2.id)
        my_model3 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model3.id)
        self.assertNotEqual(my_model2.id, my_model3.id)

    def test_str(self):
        """test the format print by the method __str__"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        output = "[BaseModel] (" + my_model.id + ")" + self.__dict__
        self.assertEqual(my_model.__str__(), output)

    def test_save(self):
        """Test if the update_at attribute is modify"""
        b1 = BaseModel()
        self.assertEqual(b1.created_at, b1.update_at)
        b1.save()
        self.isNotEqual(b1.created_at, b1.update_at)
        self.assertGreater(b1.update_at, b1.created_at)

    def test_to_dict(self):
        """Test the contain of the dictionary of an instance"""
        b2 = BaseModel()
        b2.name = "Model of Laure"
        b2.my_number = 3
        dic = {}
        dic['my_number'] = b2.number
        dic['name'] = b2.name
        dic['id'] = b2.id
        dic['created_at'] = b2.created_at.isoformat()
        dic['update_at'] = b2.update_at.isoformat()
        dic['__class__'] = 'BaseModel'
        self.assertEqual(type(b2.to_dict()), dict)
        self.assertEqual(b2.to_dict(), dic)

    if __name__ == '__main__':
        unittest.main()
