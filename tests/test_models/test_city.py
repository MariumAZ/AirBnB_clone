#!usr/bin/env python3

from models.city import City
from unittest import TestCase

class TestCity(TestCase):
    def test_state_id(self):
        self.assertIsInstance(City.state_id, str)
    def test_name(self):
        self.assertIsInstance(City.name, str)
            