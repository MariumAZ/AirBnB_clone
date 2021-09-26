#!usr/bin/env python3
"""
    Test Console
"""
from unittest import TestCase
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(TestCase):
    def test_create(self):
        """
        Tests create
        """
        #onecmd Interpret the argument as 
        #though it had been typed in response to the prompt.
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertRegex(f.getvalue(), '^Create command')
    def test_show(self):
        """
        Tests show
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertRegex(f.getvalue(), 'Show command')
    def test_create_console_fail_missing(self):
        """
        Tests create method missing class name
        """        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            expected = "** class name missing **\n"
            self.assertEqual(f.getvalue(), expected)
    def test_create_console_fail_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Paddle")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())






