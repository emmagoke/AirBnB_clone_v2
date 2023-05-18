#!/usr/bin/python3
"""
This python script contains TestCase for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import pep8
import console


class TestConsole(unittest.TestCase):
    """ This class tests console.py """
    
    @classmethod
    def setUpClass(cls):
        """ setup the console for test. """
        cls.cons = HBNBCommand()

    @classmethod
    def teardown(cls):
        """ At the end of the test will delete the console. """
        del cls.cons

    def test_pep8(self):
        """ Test if console follows pep8 rules. """
        pep_style = pep8.StyleGuide(quiet=True)
        result = pep_style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, 'Check for pep8 errors')

    def test_doctsring(self):
        """ Checks for doc strings in console.py """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_emptyline(self):
        """ Checks for empty input on the console. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """ Test the quit input command on the console. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("quit")
            self.assertEqual(None, f.getvalue())
