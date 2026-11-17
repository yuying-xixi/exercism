"""
Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
"""
def steps(number):
    """
    :param number:int -需要判断的数字
    :return steps_count:int -达到要求需要的步骤
    """
    
    # determine whether (a number) is a positive integer
    if number <=0:
        raise ValueError("Only positive integers are allowed")

    # to count steps
    steps_count = 0
    
    while number != 1:
        steps_count += 1
        
        # the number is even or odd
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

    return steps_count