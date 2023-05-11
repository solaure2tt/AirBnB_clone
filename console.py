#!/usr/bin/python3
""" This module holds our console source code """

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
