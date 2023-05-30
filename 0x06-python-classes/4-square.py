#!/usr/bin/python3
"""Define a new square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialize a square
        Args:
             size of the square
        """
        self.size = size
    @property   
    def size(self):
        """ proprety to retrive the size"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """proprety to set size to a value"""
        self.__size = value
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """return the current area"""
        return (self.__size ** 2) 
