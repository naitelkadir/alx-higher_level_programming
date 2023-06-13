#!/usr/bin/python3
"""define a function that return a dict representation of an object"""


def class_to_json(obj):
    """return a dict"""
    return obj.__dict__
