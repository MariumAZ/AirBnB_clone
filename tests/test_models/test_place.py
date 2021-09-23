#!usr/bin/env

from models.place import Place
from models.base_model import BaseModel
from unittest import TestCase

class TestPlace(TestCase):
    def test_subclass(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, "updated_at"))
    def test_city_id(self):
        self.assertIsInstance(Place.city_id, str) 
    def test_user_id(self):
        self.assertIsInstance(Place.user_id, str) 
    def test_name(self):
        self.assertIsInstance(Place.name, str)
    def test_description(self):
        self.assertIsInstance(Place.description, str)
               


