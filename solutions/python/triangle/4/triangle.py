def _is_valid_triangle(sides):
    """判断是否能构成三角形"""
    side1, side2, side3 = sides
    return side1 > 0 and side2 > 0 and side3 > 0 and side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


def equilateral(sides):
    """判断三角形是否为等边三角形"""
    if _is_valid_triangle(sides):
        side1, side2, side3 = sides
        return side1 == side2 == side3
    return False


def isosceles(sides):
    """判断三角形是否为等腰三角形"""
    if _is_valid_triangle(sides):
        side1, side2, side3 = sides
        return side1 == side2 or side1 == side3 or side2 == side3
    return False


def scalene(sides):
    """判断三角形是否为不等边三角形"""
    if _is_valid_triangle(sides):
        return not isosceles(sides)
    return False
