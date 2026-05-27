"""
to convert a number into its corresponding raindrop sounds.
"""
def convert(number):
    """
    :param number:int -给定的数字
    :return :str -返回的结果
    """
    
    is_divided_exactly_3 = (number % 3 == 0)
    is_divided_exactly_5 = (number % 5 == 0)
    is_divided_exactly_7 = (number % 7 == 0)

    raindrops_sounds = ""

    if not is_divided_exactly_3 and not is_divided_exactly_5 and not is_divided_exactly_7:
        return str(number)
    
    if is_divided_exactly_3:
        raindrops_sounds = raindrops_sounds+"Pling"

    if is_divided_exactly_5:
        raindrops_sounds = raindrops_sounds+"Plang"

    if is_divided_exactly_7:
        raindrops_sounds = raindrops_sounds+"Plong"

    return raindrops_sounds
