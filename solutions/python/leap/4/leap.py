"""
判断一年是否为闰年
"""
def leap_year(year):
    """
    :param int: year --年份
    :return bool : 闰年返回Ture,其他返回False
    """
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False
