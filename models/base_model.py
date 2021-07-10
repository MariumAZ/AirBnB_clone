#!usr/bin/env python3

import datetime 
import uuid


class BaseModel():
    def __init__(self, *args, **kwargs):
        
        if kwargs:
            for k, v in kwargs.items():
                if k  == 'created_at' :
                    self.created_at = datetime.datetime.fromisoformat(v)
                elif k  == 'updated_at' :  
                    self.updated_at = datetime.datetime.fromisoformat(v)
                elif k == 'id':
                    self.id = v   
        else:
            self.id =str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now() 
        

    def __str__(self):
        """
        custom str function
        should print: 
        [<class name>] (<self.id>) <self.__dict__>
        """    
        return "[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """
        updates the public instance attribute :
        updated_at with the current date time
        """    
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        Goal : serialization/desuerialization
        """
        dict = self.__dict__
        dict['__class__'] = self.__class__.__name__
        for k, v in dict.items():
            if k == 'created_at' or k == 'updated_at':
                dict[k] = datetime.datetime.isoformat(v)
        return dict
                

