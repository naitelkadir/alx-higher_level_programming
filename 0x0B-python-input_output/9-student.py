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

    def to_json(self):
        """return a dict representation of a class"""
        return (self.__dict__)
