#!usr/bin/env python3

from models.state import State
from unittest import TestCase
class TestState(TestCase):
    def test_name(self):
        self.assertIsInstance(State.name, str)