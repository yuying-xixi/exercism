"""
判断是否能构成三角形
"""
def _is_valid_triangle(sides):
    a, b, c =sides
    return a > 0 and b > 0 and c > 0 and a+b > c and a+c >b and b+c > a 
"""
判断三角形是否为等边三角形
"""
def equilateral(sides):
    if(_is_valid_triangle(sides)):
        a, b, c = sides
        return a == b == c
    return False

"""
判断三角形是否为等腰三角形
"""
def isosceles(sides):
    if(_is_valid_triangle(sides)):
        a, b, c = sides
        return (a == b) or (a == c) or (b == c)
    return False

"""
判断三角形是否为其他三角形
"""
def scalene(sides):
    if(_is_valid_triangle(sides)):
        return not isosceles(sides)
    return False