#!usr/bin/env python3

from unittest import TestCase
from models.user import User

class TestUser(TestCase):
    def test_email(self):
        self.assertIsInstance(User.email, str)
    def test_password(self):
        self.assertIsInstance(User.password, str)
    def test_first_name(self):
        self.assertIsInstance(User.first_name, str)
    def test_last_name(self):
        self.assertIsInstance(User.last_name, str)
                