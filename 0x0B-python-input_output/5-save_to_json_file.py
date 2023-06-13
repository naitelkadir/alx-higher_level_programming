#!/usr/bin/python3
"""define a function that writes an object to a file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
