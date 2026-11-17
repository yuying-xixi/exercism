"""
To determine whether a word or phrase is an isogram
"""
def is_isogram(string):
    """
    :param string:str -需要判断的字符串
    :return :bool
    """
    # 存储已经存在的字母
    temp_set = set()

    for letter in string:
        lower_letter = letter.lower()
        if lower_letter.isalpha():
            
            if lower_letter in temp_set:
                return False

            temp_set.add(lower_letter)

    return True
            
