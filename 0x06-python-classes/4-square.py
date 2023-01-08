#!/usr/bin/python3
""" Defines a class called square """


class Square:
    """ class square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif valuve < 0:
            raise ValueError("size must be >= 0")
        else:
            self.___size = value

    def area(self):
        return self.__size * self.__size
