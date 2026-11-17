"""
To match color and to return the index
"""
def color_code(color):
    """
    :param color:str -指定的颜色
    :return :int -对应的值
    """
    color_collection = colors()

    return color_collection.index(color)

def colors():
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
