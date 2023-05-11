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
        my_str = "[{}] ({}) ".format(type(my_model).__name__, my_model.id)
        my_str += "{}".format(my_model.__dict__)
        self.assertEqual(my_model.__str__(), my_str)

    def test_save(self):
        """Test if the update_at attribute is modify"""
        b1 = BaseModel()
        self.assertNotEqual(b1.created_at, b1.updated_at)
        update_date_prev = b1.updated_at
        b1.save()
        self.assertNotEqual(update_date_prev, b1.updated_at)
        self.assertGreater(b1.updated_at, b1.created_at)

    def test_to_dict(self):
        """Test the contain of the dictionary of an instance"""
        b2 = BaseModel()
        b2.name = "Model of Laure"
        b2.my_number = 3
        dic = {}
        dic['my_number'] = b2.my_number
        dic['name'] = b2.name
        dic['id'] = b2.id
        dic['created_at'] = b2.created_at.isoformat()
        dic['updated_at'] = b2.updated_at.isoformat()
        dic['__class__'] = 'BaseModel'
        self.assertEqual(type(b2.to_dict()), dict)
        self.assertEqual(b2.to_dict(), dic)

    def test_typeCreatedAndUnpdated(self):
        """Test if Created_at and updated_at are string"""
        b3 = BaseModel()
        self.assertEqual(type(b3.created_at), datetime.datetime)
        self.assertEqual(type(b3.updated_at), datetime.datetime)

    def test_kwargs(self):
        """Test if kwargs is correctly handle"""
        b4 = BaseModel()
        b4.mynumber = 4
        b4.name = "LaureKW"
        my_model_json = b4.to_dict()
        new_b4 = BaseModel(**my_model_json)
        self.assertEqual(new_b4.id, b4.id)
        new_b4_str = "[{}] ({}) ".format(type(new_b4).__name__, new_b4.id)
        new_b4_str += "{}".format(new_b4.__dict__)
        self.assertEqual(b4.created_at, new_b4.created_at)
        self.assertEqual(b4.updated_at, new_b4.updated_at)
        self.assertEqual(new_b4.__str__(), new_b4_str)
        self.assertEqual(type(new_b4.updated_at), datetime.datetime)
        self.assertEqual(type(new_b4.created_at), datetime.datetime)


if __name__ == '__main__':
    unittest.main()
