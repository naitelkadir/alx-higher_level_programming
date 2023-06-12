#!/usr/bin/python3
"""define a new class"""
class MyList(list):
    """My list is a class that inherts from list"""
    def print_sorted(self):
        """ a function to sort items of a list"""
        print(sorted(self))
