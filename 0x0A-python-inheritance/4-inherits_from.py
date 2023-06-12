#!/usr/bin/python3
"""define a function to verify the instance of an object"""
def inherits_from(obj, a_class):
    """return True if the object is exactly instance of the sepecified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
