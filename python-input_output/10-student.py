#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes in the list
        are retrieved.
        """

        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

        return self.__dict__
