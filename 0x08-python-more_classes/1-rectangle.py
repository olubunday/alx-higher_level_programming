#!/usr/bin/python3
'''Defines a class Rectangle'''


class Rectangle:
    '''A rectangle with size, position, and methods to calculate more'''

    def __init__(self, height=0, width=0):
        '''Initialize a rectangle with optional size'''
        self.height = height
        self.width = width

    @property
    def height(self):
        '''The height of this rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
        '''The setter ensures that the height is an integer and >= 0'''
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        '''The width of this rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
         '''The setter ensures that this value is an integer and >= 0'''
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
