import math


def calculate_hypotenuse(a, b):
    """

    Return the length of the hypotenuse

    Parameters:
    :param a: an float type length of the first perpendicular side
    :param b: an float type length of the second perpendicular side
    :precondition: a must be a float type
    :precondition: b must be a float type
    :return: the length of the hypotenuse.
    """
    length_hypotenuse = math.sqrt(a**2 + b**2)
    return length_hypotenuse
