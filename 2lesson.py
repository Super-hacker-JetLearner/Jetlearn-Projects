import random
import statistics

def linear_search(the_list:list, find):
    for index, item in enumerate(the_list):
        if item == find:
            return index
        
    return None
        

# the_list = []
# for i in range(1000):
#     the_list.append(random.randint(0, 100))
    
    
# index = linear_search(the_list, 2)
# print(index)


def binary_search(the_list:list, find):
    current_list = the_list.copy()
    index_difference = 0
    while True:
        length = len(current_list)
        if length == 0:
            return None
        half = length//2
        this_item = current_list[half]
        if find == this_item:
            real_index =  half + index_difference
            return real_index
        elif find > this_item:
            index_difference += half+1
            current_list = current_list[half+1:]
        elif find < this_item:
            current_list = current_list[:half]
            
# aaaaaa

# the_list = []
# for i in range(1000):
#     the_list.append(i)

    
# the_list = []
# for i in range(1000000):
#     the_list.append(random.randint(0, 1000))
    
# the_list.sort()
    
    
# result = binary_search(the_list, 3)
# print(result)




# def binary_search2(the_list:list[int|float], find:int|float):
#     current_range = (0, len(the_list))
#     while True:
#         print('loop')
#         print(the_list[current_range[0]:current_range[1]])
#         range = current_range[1] - current_range[0]
#         half = range//2
#         item = the_list[current_range[0]+half]
#         if find == item:
#             return half
#         elif find > item:
#             current_range = (current_range[0]+half, current_range[1])
#         elif find < item:
#             current_range = (current_range[0], current_range[1]-(half-1))
            
            
            

def binary_search3(the_list:list, find):
    current_range = (0, len(the_list))
    while the_list[current_range[0]:current_range[1]]:
        print('loop')
        # print(the_list[current_range[0]:current_range[1]])
        range = current_range[1] - current_range[0]
        half = range//2
        real_half = current_range[0]+half
        item = the_list[real_half]
        if find == item:
            return real_half
        elif find > item:
            current_range = (real_half, current_range[1])
        elif find < item:
            current_range = (current_range[0], real_half)

# aaaaaa

# the_list = []
# for i in range(1000000):
#     the_list.append(random.randint(0, 1000))
    
# the_list.sort()

# result = binary_search3(the_list, 100)
# print(result)


# print(the_list[result])

i = 0

def timing_binary_search3():
    global the_list, i
    binary_search3(the_list, i)
    
def timing_binary_search():
    global the_list, i
    binary_search(the_list, i)



import timeit


def calculate_execution_time(the_function):
    execution_time = timeit.timeit(the_function, number=1000)
    return execution_time




the_list = []
for i in range(1000000):
    the_list.append(random.randint(0, 1000))
    
the_list.sort()



def get_average():
    global the_list, i
    times = []
    for i in range(1000):
        times.append(calculate_execution_time(timing_binary_search))
    
    average = statistics.mean(times)
    
    
    