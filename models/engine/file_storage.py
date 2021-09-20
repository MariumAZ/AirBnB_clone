#!usr/bin/env python3

import json
import os
from models.base_model import BaseModel
from models import storage


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            key = str(obj.__class__.__name__) + '.' + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the json file
        """
        with open(FileStorage.__file_path, 'w') as f:
            for k, obj in FileStorage.__objects.items():
                if isinstance(obj, dict):
                    FileStorage.__objects[k] = obj
                else:    
                    FileStorage.__objects[k] = obj.to_dict()
            json.dump(FileStorage.__objects, f)     

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
                for key, v in data.items():
                    FileStorage.__objects[key] = eval(v['__class__'])(**v)
        else:
            return




    








