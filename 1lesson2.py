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
        return last_num + prev_last_num
    
    
def get_fibonacci2(length:int):
    if length > 0:
        return get_fibonacci2(length-2) + get_fibonacci2(length-1)
    else:
        return 1
    

def get_full_fibonacci(last_nums:list[int], length:int):
    if length > 0:
        sum = last_nums[-1] + last_nums[-2]
        last_nums.append(sum)
        last_nums = get_full_fibonacci(last_nums, length-1)
        return last_nums
    else:
        sum = last_nums[-1] + last_nums[-2]
        return last_nums


def get_full_fibonacci_iterate(length:int):
    last_num = 1
    last_num2 = 0
    the_list = []
    the_list.append(last_num2)
    the_list.append(last_num)
    for i in range(length):
        sum = last_num + last_num2
        last_num2 = last_num
        last_num = sum
        the_list.append(sum)
        
    return the_list


import timeit


def calculate_execution_time(the_function):
    execution_time = timeit.timeit(the_function, number=10000)
    print(f"Total time for 1000 runs: {execution_time:.6f} seconds")
    print(f"Average time per run: {execution_time / 1000:.8f} seconds")
    return execution_time



# print(get_full_fibonacci([0, 1], 500))



# print(get_full_fibonacci_iterate(500))

i = 0

def timing_full_fibonacci():
    global i
    get_full_fibonacci([0, 1], i)




def timing_full_fibonacci_iterate():
    global i
    get_full_fibonacci_iterate(i)


    
# calculate_execution_time(timing_full_fibonacci)
# calculate_execution_time(timing_full_fibonacci_iterate)



def calculate_o():
    times = []
    for i in range(1000):
        times.append(calculate_execution_time(timing_full_fibonacci_iterate))
        
    print(times)
    
    
# calculate_o()


