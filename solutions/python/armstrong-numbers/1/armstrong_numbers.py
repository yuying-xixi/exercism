"""
判断Armstrong number
"""
def is_armstrong_number(number):
    temp_number = number
    number_len = len(str(number))
    number_postion = 0
    total = 0
    
    for number_index in range(1, number_len + 1):
        # 获得数位最后一位
        temp = temp_number % 10
        total += temp**number_len

        # 排除数位最后一位
        temp_number = temp_number // 10

    return total == number
    