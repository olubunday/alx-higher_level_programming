vi #!/usr/bin/python3

"""Contains the function inherits_from"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
