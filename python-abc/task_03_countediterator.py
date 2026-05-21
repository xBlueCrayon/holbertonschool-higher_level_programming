#!/usr/bin/python3
"""Module for CountedIterator."""


class CountedIterator:
    """Iterator that counts iterated items."""

    def __init__(self, iterable):
        """Initialize iterator and counter."""

        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return iterator object."""

        return self

    def __next__(self):
        """Return next item and increment count."""

        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return iteration count."""

        return self.count
