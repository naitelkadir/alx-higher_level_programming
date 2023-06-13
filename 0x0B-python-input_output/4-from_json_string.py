#!/usr/bin/python3
""" define a function that convert a JSON string to python object"""
import json


def from_json_string(my_str):
    """return the the python obj from json string"""
    return(json.loads(my_str))
