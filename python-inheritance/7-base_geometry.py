#!/usr/bin/python3
"""This module defines a BaseGeometry class."""


class BaseGeometry:
    """This class defines a base geometry."""

    def area(self):
        """Raise exception for unimplemented area."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
