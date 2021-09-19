#usr/bin/env python3
"""
contains class BaseModel
"""
import uuid
from datetime import datetime
import time




class BaseModel():
    """"
    Base Model class
    """
    def __init__(self, *args, **kwargs) -> None:
        from models import storage
        if kwargs != {}:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = datetime.strptime(v, time_format)
                if k!= "__class__":
                    setattr(self, k, v)
        else:            
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        info = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__) 
        return info

    def save(self):
        from models import storage
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self): 
        """ returns dictionary """
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

