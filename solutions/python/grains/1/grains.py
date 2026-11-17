def square(number):
    # 异常处理
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2**(number-1)

def total():
    grains_count_total = 0
    for square_index in range(1, 65):
        grains_count_total += square(square_index)

    return grains_count_total
