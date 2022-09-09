#!/usr/bin/python3
"""Defines the function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns
   number of characters added.
    Args:
        filename (str): Name of file to be opened/created
        text (str): Text that will be inserted into file
    Returns:
        Number of characters added into file
    """
    with open(filename, 'a') as f:
        return(f.write(text))
