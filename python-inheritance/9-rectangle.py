#!/usr/bin/python3
"""This module defines a Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle area."""

        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""

        return "[Rectangle] {}/{}".format(self.__width,
                                          self.__height)
