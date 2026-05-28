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
        
        if number not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"}:
            return False
        
        if number == "X":
            if index == 9:
                number = "10"
            else:
                return False

        total += int(number) * (10 - index)

        
    return total % 11 == 0
        