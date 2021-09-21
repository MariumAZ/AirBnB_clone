#!/usr/bin/python3
""" console """

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command console
    """
    
    prompt = '(hbnb)'
    intro = "-------------- Welcome to AirBnB console --------------  "
   
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()





