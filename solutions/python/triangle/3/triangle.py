"""判断是否能构成三角形"""
def _is_valid_triangle(sides):
    side1, side2, side3 = sides
    return side1 > 0 and side2 > 0 and side3 > 0 and side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


"""判断三角形是否为等边三角形"""
def equilateral(sides):
    if _is_valid_triangle(sides):
        side1, side2, side3 = sides
        return side1 == side2 == side3
    return False


"""判断三角形是否为等腰三角形"""
def isosceles(sides):
    if _is_valid_triangle(sides):
        side1, side2, side3 = sides
        return side1 == side2 or side1 == side3 or side2 == side3
    return False


"""判断三角形是否为其他三角形"""
def scalene(sides):
    if _is_valid_triangle(sides):
        return not isosceles(sides)
    return False
