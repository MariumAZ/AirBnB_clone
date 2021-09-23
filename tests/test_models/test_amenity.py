#!usr/bin/env python3

from models.amenity import Amenity
from unittest import TestCase

class TestAmenity(TestCase):
    def test_name(self):
        self.assertIsInstance(Amenity.name, str)
