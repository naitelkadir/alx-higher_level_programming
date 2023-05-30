#!/usr/bin/python3
"""Define a new square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a square
        args: size of the square
        """
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """ a function to return a current square"""
        return (self.__size ** 2)
