#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""define a new class"""
class Rectangle(BaseGeometry):
    """ define a class child of baseGeometry"""
    def __init__(self, width, height):
        """initiliaze the class
        Args:
            width(int): the width of the rectangle
            height: the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
