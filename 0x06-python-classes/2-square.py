#!/usr/bin/python3
"""Reprsent a square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Intialize a new Square
        Args:
            size(int): the size of the new square
        """
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
