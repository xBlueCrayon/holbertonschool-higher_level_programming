#!/usr/bin/python3
"""This module defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square."""

    def __init__(self, size):
        """Initialize the square."""

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
