#!/usr/bin/python3
""" console """

import cmd
from models.base_model import BaseModel
import shlex
from models import storage

class_names = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """
    Command console
    """
    
    prompt = '(hbnb)'
    #intro = "-------------- Welcome to AirBnB console --------------  "
   
    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True
    def do_EOF(self, arg):
        """ Exits console """
        return True
    def emptyline(self) -> bool:
        return False    
    def do_help(self, arg: str) :
        """ help methods"""
        return super().do_help(arg)
    def do_create(self, args):
        """ creates new instance """
        if len(args) == 0:
            print("** class name missing **")
            return  
        l = shlex.split(args)
        c_name = l[0]
        if c_name in class_names:
            new_instance = class_names[c_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")  
    def do_show(self, args):
        """Prints an instance as a string based on the class and id"""
        l = shlex.split(args)
        if len(l) == 0:
            print("** class name missing **")
            return    
        c_name = l[0] 
        if c_name not in class_names:    
            print("** class doesn't exist **")
            return
        if len(l) == 1:
            print("** instance id missing ** ")
            return
        if len(l) > 1 :
            dic_objects = storage.all()
            id = l[1]
            key = c_name + '.' + id
            if key not in dic_objects:
                print("** no instance found **")
                return
            else:
                print(dic_objects[key])
if __name__ == '__main__':
    HBNBCommand().cmdloop()





