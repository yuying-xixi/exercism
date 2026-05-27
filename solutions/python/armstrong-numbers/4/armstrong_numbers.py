"""
判断Armstrong number
"""

def is_armstrong_number(number):
    """
    :param number(int): 需要判断的数
    :return bool: 是否为水仙花数
    """
    temp_number = number
    number_count = len(str(number))
    total = 0
    
    while temp_number > 0:
        # 获得数位最后一位
        digit = temp_number % 10
        total += digit**number_count

        # 排除数位最后一位
        temp_number = temp_number // 10

    return total == number
    