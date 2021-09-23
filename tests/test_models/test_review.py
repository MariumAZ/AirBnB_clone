#!usr/bin/env python3

from models.review import Review
from unittest import TestCase

class TestReview(TestCase):
    def test_place_id(self):
        self.assertIsInstance(Review.place_id, str)
    def test_user_id(self):
        self.assertIsInstance(Review.user_id, str)
    def test_text(self):
        self.assertIsInstance(Review.text, str)
            
