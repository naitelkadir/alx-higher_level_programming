#!/usr/bin/python3
"""define a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """ add a new attribute to an object if possible.
    Args:
        obj(any): the object to add an attribut to
        att(str): the name of the attribute to add
        value(any): the value of att
    Raises:
        TypeError: if the attribute can not be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
