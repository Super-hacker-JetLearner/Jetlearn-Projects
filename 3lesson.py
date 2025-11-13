# list sorting
import random

def one_iteration(the_list:list):
    current_list = the_list
    current_index = 0
    while True:
        if current_list[current_index] > current_list[current_index+1]:
            first_item = current_list[current_index]
            second_item = current_list[current_index+1]
            current_list[current_index] = second_item
            current_list[current_index+1] = first_item
            current_index += 1
        else:
            current_index += 1
            
        if current_index+1 == len(current_list):
            return current_list


def bubble_sort(the_list:list):
    if len(the_list) == 1:
        return the_list
    current_list = the_list
    for i in the_list:
        current_list[:-1] = one_iteration(current_list)[:-1]
        
    return current_list



the_list = []
for i in range(10):
    the_list.append(random.randint(0, 10))
    
    
# result = bubble_sort(the_list)
# print(result)


def one_insertion(the_list:list, index):
    while True:
        print(index)
        if index == 0:
            return the_list
        before_number = the_list[index-1]
        this_number = the_list[index]
        if before_number > this_number:
            before_item = the_list[index-1]
            the_list[index-1] = this_number
            the_list[index] = before_item
            index -= 1
            
        else:
            return the_list
            
        if index == 0:
            return the_list
        
        


def insertion_sort(the_list:list):
    current_list = the_list
    for i in range(1, len(the_list)):
        current_list = one_insertion(current_list, i)
        
    return current_list


result = insertion_sort([2, 1])
print(result)