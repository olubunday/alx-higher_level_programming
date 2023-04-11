#!/usr/bin/python3

"""Program contains a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __equal__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __negate__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
