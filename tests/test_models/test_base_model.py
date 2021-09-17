#!usr/bin/python3

"""
Test BaseModel 
"""

from datetime import datetime
from models.base_model import BaseModel
from unittest import TestCase

class TestBaseModel(TestCase):
    def test_instance_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1, bm2)
    def test_type_updated_at(self):
        bm = BaseModel()
        updated_at = bm.updated_at
        self.assertIsInstance(updated_at, datetime)
    def test_to_dict(self):
        bm = BaseModel()
        bm.name = "Myriam"
        bm.sport = "paddle"
        bm_dic = bm.to_dict()
        id = bm.id
        bm_c = bm.created_at.isoformat()
        bm_u = bm.updated_at.isoformat()
        expected_dic = {"name":"Myriam", "sport":"paddle","id":id, "created_at":bm_c, "updated_at":bm_u } 
        self.assertEqual(bm_dic, expected_dic)
    def test_save(self):
        bm = BaseModel()
        actual_time = datetime.now()
        up = bm.updated_at()
        self.assertEqual(up, actual_time)

