"""模块功能：计算棋盘麦粒相关问题"""

def square(number):
    """计算指定方格的麦粒数量，范围1-64"""
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """计算64格棋盘总共麦粒数量"""
    grains_count_total = 0
    for square_index in range(1, 65):
        grains_count_total += square(square_index)

    return grains_count_total
