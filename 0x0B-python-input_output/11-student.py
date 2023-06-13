#!/usr/bin/python3
"""Define a new student class"""


class Student:
    """Represent the student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the student class.

        Args:
            first_name(str): the first name
            last_name(str): the last name
            age(int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,  attrs=None):
        """return a dict representation of a class

        Args:
             attrs(list): the list of attributes
        """
        if attrs == None:
            return (self.__dict__)
        d = {}
        for x in attrs:
            for y in (self.__dict__):
                if x == y:
                    d[x] = self.dict[y]
        return (d)
    def reload_from_json(self, json):
        """a function that replaces all attributes of an instance.
        
        Args:
            json: a dictionnary
        """
        for i, j in json.items():
            setattr(self, k, v)
