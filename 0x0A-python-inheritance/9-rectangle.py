#!/usr/bin/python3
"""define a class rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""
    def __init__(self, width, height):
        """initiliaze a new rectangle.
        Args:
            width(int): the width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)
    def __str__(self):
        """return the print() and str() representation of the rectangle"""
        s = "[" + str(self.__class__.__name__) + "] "
        s += str(self.__width) + "/" + str(self.__height)
        return (s)
