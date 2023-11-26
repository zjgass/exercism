def equilateral(sides):
    """

    :param sides: list - the sides to test
    :return: bool - is the triangle equilateral
    """
    
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return (is_triangle(sides)
            and a == b and b == c)


def isosceles(sides):
    """

    :param sides: list - the sides to test
    :return: bool - is the triangle isosceles
    """

    a = sides[0]
    b = sides[1]
    c = sides[2]

    return (is_triangle(sides)
            and (a == b or b == c or a == c))


def scalene(sides):
    """

    :param sides: list - the sides to test
    :return: bool is the triangle scalene
    """

    a = sides[0]
    b = sides[1]
    c = sides[2]

    return (is_triangle(sides)
            and a != b and b != c and a != c)

def is_triangle(sides):
    """

    :param sides: int - the list of sides to test
    :return: bool - is a valid triangle
    """

    a = sides[0]
    b = sides[1]
    c = sides[2]

    return (a > 0 and b > 0 and c > 0
            and a + b >= c and b + c >= a and a + c >= b)
