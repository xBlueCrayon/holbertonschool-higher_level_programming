#!/usr/bin/python3
"""This module defines inherits_from."""


def inherits_from(obj, a_class):
    """Return True if obj inherited from a_class."""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
