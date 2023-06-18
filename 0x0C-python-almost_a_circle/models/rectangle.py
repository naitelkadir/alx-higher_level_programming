#!/usr/bin/python3
from models.base import Base
"""Define a new class rectangle inherted from base"""


class Rectangle(Base):
    """represent rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a rectangle class.

        Args:
            x: x
            y: y
            width: width
            height: height
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        """get the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value)!= int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the width"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the width"""
        if type(value)!= int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """get the width"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set the width"""
        if type(value)!= int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """get the width"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set the width"""
        if type(value)!= int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the rectangle"""
        return (self.__width * self.__height)
    def display(self):
        """display rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for k in range(self.__y):
            print("")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")
    def __str__(self):
        """represent the rectangle"""
        return ("[" + self.__class__.__name__ + "] (" + str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height))
    def update(self, *args, **kwargs):
        """a method that assigns argument to each attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None: 
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height == arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    def to_dictionary(self):
        """ represent the rectangle class as a dictionnary"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
