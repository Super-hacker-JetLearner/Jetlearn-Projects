my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set)

other_set = {"hello", "world", 1, 2, 3, False, 0}
print(other_set)

my_set.add(11)
print(my_set)

print(len(other_set))

for i in other_set:
    print(i)
    

if "hello" in other_set:
    print("hello is in other_set")
    
    
other_set.remove("hello")
print(other_set)

if "no" in other_set:
    other_set.remove("no")
    
other_set.discard(1)

print(other_set)

other_set.pop()

print(other_set)


# other_set.clear()
print(other_set)

# del other_set

# print(other_set)

# print(other_set[0])

# set3 = my_set.union(other_set)

set3 = my_set|other_set

print(set3)


my_set.update(other_set)
print(my_set)

set4 = my_set.intersection(other_set)
print(set4)


set5 = my_set & other_set
print(set5)

set6 = my_set.symmetric_difference(other_set)
print(set6)

set7 = my_set ^ other_set
print(set7)


my_set.symmetric_difference_update(other_set)
print(my_set)

