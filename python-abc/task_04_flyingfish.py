#!/usr/bin/python3
"""Module for multiple inheritance example."""


class Fish:
    """Fish class."""

    def swim(self):
        """Print swimming message."""

        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""

        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Print flying message."""

        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class."""

    def swim(self):
        """Override swim method."""

        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method."""

        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method."""

        print("The flying fish lives both in water and the sky!")
