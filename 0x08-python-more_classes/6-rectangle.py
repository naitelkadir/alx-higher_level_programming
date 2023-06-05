#!/usr/bin/python3
"""Define a new rectangle class"""
class Rectangle:
    """Represent a rectangle
    Attributes:
           number_of_instances(int)
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """initialize a rectangle class.
        Args:
           width: width of the rectangle
           height: height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
    @property
    def width(self):
        """get the width"""
        return(self.__width)
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """get the height"""
        return(self.__height)
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """ return the area of the rectangle"""
        return (self.__width * self.__height)
    def perimeter(self):
        """ return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.height))
    def __str__(self):
        """represent the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        new = []
        for i in range(self.__height):
            for j in range(self.__width):
                new.append("#")
            if i != self.__height - 1:
                new.append("\n")
        return ("".join(new))
    def __repr__(self):
        """ represent the rectangle"""
        new = "Rectangle(" + str(self.__width)
        new += "," + str(self.__height) + ")"
        return (new)
    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
    

