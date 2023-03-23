#!/usr/bin/python3
"""
This python script contains TestCase for console.py
"""
import unittest
from console import HBNBCommand
import pep8
import console


class TestConsole(unittest.TestCase):
    """ This class tests console.py """

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
