import random


def binary_search_recursion(the_list:list, find):
        the_range = len(the_list)
        half = the_range//2
        if the_range == 0:
            return False
        if the_range == 1:
            if the_list[0] == find:
                return 0
            else:
                return False

        item = the_list[half]
        if find == item:
            return half
        elif find > item:
            result = binary_search_recursion(the_list[half:], find)
            return half + result
        elif find < item:
            result = binary_search_recursion(the_list[:half], find)
            return result




the_list = []
for i in range(100):
    the_list.append(random.randint(0, 10))

the_list.sort()


result = binary_search_recursion(the_list, 9)
print(result)

print(the_list[result])
print(the_list)
