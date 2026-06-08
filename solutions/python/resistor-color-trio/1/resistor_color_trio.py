"""
计算指定颜色组合代表的欧姆值
"""
def label(colors):
    """
    :param colors:list -给定的颜色组合
    :return :int -计算后的值
    """
    
    colors_collection = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
    }

    ten_digit_place = colors_collection.get(colors[0], 0)
    ones_digit_place = colors_collection.get(colors[1], 0)
    multiplier = colors_collection.get(colors[2], 0)

    value = (ten_digit_place*10 + ones_digit_place) * 10**multiplier

    if value == 0:
        return "0 ohms"

    if value % 1_000_000_000 == 0:
        return f"{value // 1_000_000_000} gigaohms"
    elif value % 1_000_000 == 0:
        return f"{value // 1_000_000} megaohms"
    elif value % 1_000 == 0:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"
        
