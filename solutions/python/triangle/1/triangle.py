def is_a_triangle(sides):
    '''
    Defines if the sides form a triangle by checking if the sides are greater than 0 and if the sum of any two sides is greater than owr equal to the third

    Args:
        sides (list): List of sides of a triangle

    Returns:
        bool: True if the sides form a triangle, False otherwhise
    '''
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]

    return side_a + side_b >= side_c and side_b + side_c >= side_a and side_a + side_c >= side_b and side_a > 0 and side_b > 0 and side_c > 0
    
def equilateral(sides):
    '''
    Defines if a triangle is an equilateral one

    Args:
        sides (list) : List of sides of a triangle

    Returns: 
        bool: True if it is a equilateral triangle, False otherwhise
    '''
    return is_a_triangle(sides) and sides[0] == sides[1] and sides[1] == sides[2]
    
def isosceles(sides):
    '''
    Defines if a triangle is an isosceles one

    Args:
        sides (list) : List of sides of a triangle

    Returns: 
        bool: True if it is a isosceles triangle, False otherwhise
    '''
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    
    return is_a_triangle(sides) and (side_a == side_b or side_b == side_c or side_c == side_a)


def scalene(sides):
    '''
    Defines if a triangle is an scalene one

    Args:
        sides (list) : List of sides of a triangle

    Returns: 
        bool: True if it is a scalene triangle, False otherwhise
    '''
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    return is_a_triangle(sides) and side_a != side_b and side_b != side_c and side_a != side_c
