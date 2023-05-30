#!/usr/bin/python3
"""Define a new square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize a square
        Args:
            size(int): size of the square
            position(int, int): position of the square
        """
        self.size = size
        self.position = position
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
    @property
    def position(self):
        """ proprety to retrive the position"""
        return (self.__position)
    @position.setter
    def position(self, value):
        """proprety to set position to a value"""
        self.__position = value
        if not type(value) is tuple or len(value) != 2 or not type(value[0]) is int or not type(value[1]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        """return the current area"""
        return (self.__size ** 2)
    def my_print(self):
        """method to print the square"""
        if (self.size == 0):
            print("")
            return
        for m in range(0, self.__position[1]):
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
