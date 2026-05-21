#!/usr/bin/python3
"""Module for abstract Animal class."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class."""

    @abstractmethod
    def sound(self):
        """Abstract sound method."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return dog sound."""

        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return cat sound."""

        return "Meow"
