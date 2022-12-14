#!/usr/bin/python3
"""Import Rectangle"""

Rectangle = __import__('7-rectangle').Rectangle

"""Defines class Square that inherits from Rectangle"""


class Square(Rectangle):
    """Define variable or attribute"""
    def __init__(self, size):
        """Validates values with integer_validator"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return area of square"""
        return self.__size * self.__size
