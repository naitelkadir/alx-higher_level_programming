#!/usr/bin/python3
""" define a function that convert an object to JSON representation"""
import json


def to_json_string(my_obj):
    """return the json representation"""
    return (json.dumps(my_obj))
