"To reversed string"
def reverse(text):
    """
    :param text:str -需要被反转的字符串
    :return :str -完成反转的字符串
    """

    reversed_iter = reversed(text)
    
    return "".join(reversed_iter)
