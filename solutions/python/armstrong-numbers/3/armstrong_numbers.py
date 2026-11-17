"""
判断Armstrong number
"""

def is_armstrong_number(number):
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
    