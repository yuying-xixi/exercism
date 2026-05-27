"""
To determine whether a number is perfect, abundant, or deficient
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    # To determine whether the number is postive integer
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor

    if number == sum:
        return "perfect"
    elif number < sum:
        return "abundant"
    else:
        return "deficient"
