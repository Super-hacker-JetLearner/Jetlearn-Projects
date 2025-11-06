

def get_factorial(number:int):
    if number > 1:
        return number * get_factorial(number-1)
    return 1


# print(get_factorial(52))



def get_fibonacci(last_num:int, prev_last_num:int, length:int):
    if length > 0:
        sum = last_num + prev_last_num
        return get_fibonacci(sum, last_num, length-1)
    else:
        return 1
    
    
print(get_fibonacci(1, 1, 5))

