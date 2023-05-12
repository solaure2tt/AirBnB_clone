#!/usr/bin/python3
""" This module holds our console source code """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This is the blue print for our console class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ This method exits the console """

        return True

    def do_EOF(self, arg):
        """ This method exits the console """

        return True

    def emptyline(self):
        """ Overriding base class method to do nothing """
        pass

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                my_model = BaseModel()
                my_model.save()
                print("{}".format(my_model.id))
            else:
                print("** class doesn't exist **")

    def help_create(self):
        print('create class_name'), '\n'
        print('create a new instance of class_name')

    def do_show(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            if args[0] == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = 0
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            ob = all_objs[obj_id]
                            print(ob)
                            find = 1
                            break
                    if find == 0:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_show(self):
        print('show class_name id_instance'), '\n'
        print('Prints the string representation of an instance')

    def do_destroy(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            if args[0] == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = 0
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            ob = all_objs[obj_id]
                            storage.destroy_objects(obj_id)
                            storage.save()
                            find = 1
                            break
                    if find == 0:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_destroy(self):
        print('destroy class_name id_instance'), '\n'
        print('Deletes an instance based on the class name and id')

    def do_all(self, arg):
        all_objs = storage.all()
        if arg == "":
            for obj_id in all_objs.keys():
                print(all_objs[obj_id])
        else:
            if arg == "BaseModel":
                for obj_id in all_objs.keys():
                    obj_split = obj_id.split(".")
                    if obj_split[0] == arg:
                        print(all_objs[obj_id])
            else:
                print("** class doesn't exist **")

    def help_all(self):
        print('all [class_name]'), '\n'
        print('Prints all string representation \
of all instances based or not on the class name')

    def do_update(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            if args[0] == "BaseModel":
                if len(args) < 4:
                    if len(args) == 1:
                        print("** instance id missing **")
                    if len(args) == 2:
                        print("** attribute name missing **")
                    if len(args) == 3:
                        print("** value missing **")
                else:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = 0
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            storage.update_objects(obj_id, args[2], args[3])
                            storage.save()
                            find = 1
                            break
                    if find == 0:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_update(self):
        print('update class_name id_instance key value'), '\n'
        print('Updates an instance based on the class name and id \
by adding or updating attribute')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
