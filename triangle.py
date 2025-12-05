def area(a, h): 
    '''
    Returns the area of the triangle.

        Parameters:
            a (float): the length of the side of the triangle
            h (float): height lowered to the side with length a
        
        Return value:
            a * h /2 (float): the area of the triangle with side a
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Returns the perimeter of the triangle.

        Parameters:
            a (float), b (float), c (float): the lengths of the sides of the triangle
            
        Return value:
            a + b + c (float): the perimeter of a triangle with sides a, b, c
    '''
    return a + b + c 