#!/usr/bin/python3
"""Import BaseGeometry"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

"""Defines class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Define variable or attribute"""
    def __init__(self, width, height):
        """Validates values with integer_validator"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return dimensions of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
