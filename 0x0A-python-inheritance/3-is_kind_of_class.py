#!/usr/bin/python3
"""define a function to verify the instance of an object"""
def is_kind_of_class(obj, a_class):
    """return True if the object is exactly instance of the sepecified class"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
