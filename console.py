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
    def do_show1(self, args):
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
    def do_show(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_names:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")           
    def do_destroy(self, args):
        """ destroys an instance """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_names:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **") 

    def do_all(self, args):
        """ Prints all string representation of all instances""" 
        args = shlex.split(args)
        if len(args) == 0:
            print([storage.all()])
            return 
        if len(args) == 1:
            result = []
            c_name = args[0]
            if c_name in class_names:
                for k, v in storage.all().items():
                    if k.split('.')[0] == c_name:
                        result.append(str(storage.all()[k]))
                        print(result)           
            else:
                print("** class doesn't exist **") 

    def do_update(self, args):
        """ Updates an instance based on the class name """   
        args = shlex.split(args)        
        if len(args) == 0:
            print("** class name missing **")      
        elif args[0] in class_names:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[k], args[2], args[3])
                            storage.save()
                        else:
                            print("** value missing **")     
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")     
            else:
                print('** instance id missing **')
        else:
            print("** class doesn't exist **")                    
                        
if __name__ == '__main__':
    HBNBCommand().cmdloop()





