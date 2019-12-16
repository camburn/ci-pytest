""" An example project to test CI on """
from collections import namedtuple


Vector3 = namedtuple('Vector3', ['x', 'y', 'z'])

class Square:
    """ A Square class for doing square things """
    def __init__(self, position, size):
        """ Create a new square

        Args:
            position: center position of square
            size: the length of a side
        """
        self.position = position
        self.size = size

    def perimeter(self):
        """ Return perimeter of this square """
        return self.size * 4

    def area(self):
        """ Return area of this square """
        return self.size ** 2
