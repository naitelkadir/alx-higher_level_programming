#!/usr/bin/python3
"""define a function that creates an object from Json file"""
import json


def load_from_json_file(filename):
    """create an object from Json file"""
    with open(filename) as f:
       return  json.load(f)
