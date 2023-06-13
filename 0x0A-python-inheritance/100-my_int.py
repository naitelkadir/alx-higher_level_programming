#!/usr/bin/python3
"""define a class Myint inherits from int"""


class MyInt(int):
    """inverts == and != int operators"""
    def __eq__(self, value):
        """invert to == to !="""
        return self.real != value
    def __ne__(self, value):
        """inverts != to =="""
        return self.real == value
