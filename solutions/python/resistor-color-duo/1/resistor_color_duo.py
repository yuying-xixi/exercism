"""
给定颜色列表，返回前两个元素组合的值
"""
def value(colors):
    """
    :param colors:list -给定的颜色列表
    :return :int -返回对应的电阻值
    """
    colors_collaction = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }

    resistors_value = ""

    for index in range(0,2):
        resistors_value += colors_collaction.get(colors[index], "")

    return int(resistors_value)
