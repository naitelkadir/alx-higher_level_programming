#!/usr/bin/python3
"""define a class square inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle"""
    def __init__(self, size):
        """initiliaze a new rectangle.

        Args:
            size(int): the width of the rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
