import random

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
            


# the_list = []
# for i in range(1000):
#     the_list.append(i)

    
the_list = []
for i in range(1000000):
    the_list.append(random.randint(0, 1000))
    
the_list.sort()
    
    
result = binary_search(the_list, 3)
print(result)



