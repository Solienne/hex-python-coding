#!/usr/bin/python3
"""Creating class Square"""


class Square:
    """Derives a square"""
    def __init__(self, size):
        """initializes attributes
        Args:
            size (int): value to initialize `size`
        See:
            ``Args`` section doesn't include `self` parameter.
        """
        self.__size = size
