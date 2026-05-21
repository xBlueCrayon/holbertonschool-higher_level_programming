#!/usr/bin/python3
"""Module for shapes and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Shape class."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle."""

        self.radius = abs(radius)

    def area(self):
        """Return circle area."""

        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""

        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""

        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""

        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""

        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape area and perimeter."""

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
    