#!/usr/bin/python3
""" define a nex class"""
class LockedClass:
    """hat prevents the user from dynamically creating new instance attributes
    """
    __slots__("first_name")
