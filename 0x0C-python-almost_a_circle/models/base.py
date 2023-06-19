#!/usr/bin/python3

import json
"""Define a new class called Base"""


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a base class.
        
        Args:
           id(int): The identity of the new Base.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert a list to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """write json string to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                lists_dic = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(lists_dic))
    @staticmethod
    def from_json_string(json_string):
        """return the list represent by json string"""
        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """return the instance with all attribute"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return (new)
    @classmethod
    def load_from_file(cls):
        """return the list of all the instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return ([])
