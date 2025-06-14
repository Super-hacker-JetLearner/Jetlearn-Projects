import random


marks = []
for i in range (20):
    marks.append(random.randint(0,100))
    

first_list = []
for i in marks:
    if i <= 30:
        first_list.append(i)


second_list = []
for i in marks:
    if 30<i<70:
        second_list.append(i)
 
 
third_list = []
for i in marks:
    if i >= 70:
        third_list.append(i)



print(marks)
print(first_list)
print(second_list)
print(third_list)
