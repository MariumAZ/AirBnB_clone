#! usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command console
    """
    intro = "-------------- Welcome to AirBnB console --------------  "
    prompt = '(hbnb) '
   
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





