#!/usr/bin/python3
'''class that defines a rectangle'''


class Rectangle:
    '''My rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialize a rectangle with optional size'''

        self.height = height
        self.width = width

    @property
    def height(self):
        '''
        The height of this rectangle
        The setter ensures that this value is an integer and >= 0
        '''

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        '''
        The width of this rectangle
        The setter ensures that this value is an integer and >= 0
        '''

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    def area(self):
        '''Returns the area of the rectangle'''

        return self.__height * self.__width

    def perimeter(self):
        '''Returns the perimeter of the rectngle''' 

        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
