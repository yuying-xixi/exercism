"""三角形类型判断工具模块，提供合法校验、等边/等腰/不等边三角形判断"""

def _is_valid_triangle(sides):
    """判断是否能构成合法三角形"""
    side1, side2, side3 = sides
    # 简化链式比较，消除 R1716
    return 0 < side1 and 0 < side2 and 0 < side3 \
        and side1 + side2 > side3 \
        and side1 + side3 > side2 \
        and side2 + side3 > side1


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
