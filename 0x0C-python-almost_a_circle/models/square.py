#!/usr/bin/python3
from models.rectangle import Rectangle
"""Define a new class square inherted from rectangle"""


class Square(Rectangle):
    """represent a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square class.
        
        Args:
            size: the size of the square
            x: the x position
            y: the y position
            id: the id of the square
        """
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """get the size of the squre"""
        return (self.width)
    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value
    def __str__(self):
        """represent the rectangle"""
        return ("[Square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width))
    def update(self, *args, **kwargs):
        """a method that assigns argument to each attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x == arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    def to_dictionary(self):
        """represent the square class as a dictionnary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y":self.y}
