#!/usr/bin/python3
"""Creating class Square"""


class Square:
    """Derives square"""
    def __init__(self, size=0):
        """initializes attributes
        Args:
            size (int): size of the square
        See:
            ``Args`` section doesn't include `self` parameter
        Raises:
            TypeError: if `size` isn't an integer
            ValueError: if `size` is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of square
        Returns:
            area of square
        """
        return (self.__size ** 2)
