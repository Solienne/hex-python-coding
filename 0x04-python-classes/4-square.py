#!/usr/bin/python3
"""Creating class Square"""


class Square:
    """Derives square"""
    def __init__(self, size=0):
        """initializes attributes
        Args:
            size (int): size of square
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

    @property
    def size(self):
        """Property to retrive value of `size`"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of `value`
        Args:
            value (int): value to be set to `value`
        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square in stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
