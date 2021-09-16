#usr/bin/env python3

import uuid
from datetime import datetime
import time

class BaseModel():
    """"
    Base Model class
    """
    def __init__(self) -> None:
        #have a unique id for each model 
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self) -> str:
        info = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__) 
        return info
    def save(self):
        """
        updates the public instance attribute with the current datetime 
        """      
        self.updated_at = datetime.now()
    def to_dict(self):
        """
        returns all the keys/values of __dict__ of the innstance 
        """    
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        #convert created_at and updated_at to string in ISO format
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic



