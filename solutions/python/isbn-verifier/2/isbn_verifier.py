"""
To determine whether a given ISBN is valid
"""
def is_valid(isbn):
    """
    :param isbn:str -需要判断的ibsn
    :return :bool
    """

    # 统计isbn数字和
    total = 0
    
    # 去掉 -
    isbn = isbn.replace("-", "")

    # 长度必须为10
    if len(isbn) != 10:
        return False
    
    for index, number in enumerate(isbn):
        
        if not (number.isdigit() or number == "X"):
            return False
        
        if number == "X":
            if index == 9:
                value = 10
            else:
                return False
        
        elif number.isdigit():
            value = int(number)
        
        else:
            return False
        
        total += value * (10 - index)

    return total % 11 == 0
        