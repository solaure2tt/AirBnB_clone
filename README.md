# THIS PROJECT (HBNB) IS A CLONE OF AIRBNB
(which is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences)

This project will be done in stages.

#  1. THE CONSOLE
Here we will be making a CLI to manage our objects. In order to achieve this, we will follow the underlisted steps:

- Create a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine.
