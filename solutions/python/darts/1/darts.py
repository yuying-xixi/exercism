"""
击中标靶得分统计
"""
def score(x, y):
    """
    :param x:int -击中标靶心的横坐标
    :param y:int -击中标靶心的纵坐标
    :return :int -得分
    """
    pi = 3.14

    # 计算以靶心为圆心,圆心到命中的点为半径的圆面积
    area = pi * (x**2 + y**2)

    # radius <= 1
    if area <= pi:
        return 10
    # radius <= 5
    if area <= pi * 25:
        return 5
    # radius <= 10
    if area <= pi * 100 :
        return 1
    # # radius > 10
    else:
        return 0