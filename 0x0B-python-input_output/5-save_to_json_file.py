#!/usr/bin/python3
"""define a function that writes an object to a file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file"""
    s = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(s)
