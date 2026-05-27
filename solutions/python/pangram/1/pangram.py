"""
 To figure out if a sentence is a pangram.
"""
def is_pangram(sentence):
    """
    :param sentence:str -需要判断的句子
    :return :bool -是否是pangram
    """

    # 使用集合去除句子重复字母
    temp_set = set()
    
    for letter in sentence:
        if letter.isalpha():
            temp_set.add(letter.lower())

    return len(temp_set) == 26