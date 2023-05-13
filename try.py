#!/usr/bin/python3


from models.base_model import BaseModel

b4 = BaseModel()
b4.mynumber = 4
b4.name = "LaureKW"
my_model_json = b4.to_dict()
print(b4.id)
new_b4 = BaseModel(**my_model_json)
new_b4_str = "[{}] ({}) ".format(type(new_b4).__name__, new_b4.id)
new_b4_str += "{}".format(new_b4.__dict__)

print(b4)
