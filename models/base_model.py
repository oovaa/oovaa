#!/usr/bin/python3
"""base modle"""

import datetime
import uuid


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k in ('__class__'):
                    continue
                if k in ('created_at', 'updated_at'):
                    setattr(self, k, datetime.datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        # TODO: created_at and updated_at must be converted to string object in ISO format:
        # format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        # you can use isoformat() of datetime object
        # fixed
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = obj_dict['created_at'].isoformat()

        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
