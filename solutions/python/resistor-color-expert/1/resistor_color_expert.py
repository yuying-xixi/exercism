"""
To clearly display required information about resistor
"""
def resistor_label(colors):
    """
    :param colors:list -给定的颜色带
    :return :str -指定显示的电阻信息
    """
    
    colors_collection = {
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

    tolerance_colors = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}
    colors_length = len(colors)

    if colors_length == 1:
        return f"{colors_collection.get(colors[0], 0)} ohms"
        
    value = ""
    for index in range(0, colors_length -2):
        value += colors_collection.get(colors[index], 0)
    
    tolerance = tolerance_colors.get(colors[-1], "")
    power = int(colors_collection.get(colors[-2], "0"))
    resistor_value = int(value + "0" * power)

    if resistor_value // 1_000_000_000 != 0:
        return f"{resistor_value / 1_000_000_000} gigaohms ±{tolerance}"
        
    if resistor_value // 1_000_000 != 0:
        return f"{resistor_value / 1_000_000} megaohms ±{tolerance}"
        
    if resistor_value // 1_000 != 0:
        temp_value = resistor_value / 1_000
        if int(temp_value) == float(temp_value):
            temp_value = int(temp_value)
        return f"{temp_value} kiloohms ±{tolerance}"

    return f"{resistor_value} ohms ±{tolerance}"
