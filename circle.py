import math


def area(r):
    '''
    Returns the area of the circle.

        Parameters:
            r (float): the radius of the circle
        
        Return value:
            math.pi * r * r (float): the area of a circle with radius r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of the circle.

        Parameters:
            r (float): the radius of the circle
        
        Return value:
            2 * math.pi * r (float): the perimeter of a circle with radius r
    '''
    return 2 * math.pi * r
