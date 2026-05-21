#!/usr/bin/python3
"""Module for mixins and Dragon class."""


class SwimMixin:
    """Mixin for swimming."""

    def swim(self):
        """Print swim message."""

        print("The creature swims!")


class FlyMixin:
    """Mixin for flying."""

    def fly(self):
        """Print fly message."""

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class."""

    def roar(self):
        """Print roar message."""

        print("The dragon roars!")
