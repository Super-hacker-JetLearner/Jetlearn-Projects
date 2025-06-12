the_list = [[1,2,3],
            [4,5,6],
            [7,8,9]]

for i in range(len(the_list)):
    for j in range (len(the_list[i])):
        print(the_list[i][j])
        
        
for i in the_list:
    print(" ".join(map(str, i)))
    
rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
new_list = []
for i in range(rows):
    new_list.append([])
    for j in range(columns):
        new_list[i].append(input(f"enter the value of row {i}, column {j}: "))
        
for i in new_list:
    print(" ".join(map(str, i)))
    
    
print("here is the second list")

other_list = []
for i in range(rows):
    other_list.append([])
    for j in range(columns):
        other_list[i].append(input(f"enter the value of row {i}, column {j}: "))
        
for i in other_list:
    print(" ".join(map(str, i)))
    
    
answer_list = []
for i in range(rows):
    answer_list.append([])
    for j in range(columns):
        answer_list[i].append(int(new_list[i][j]) + int(other_list[i][j]))
        
print("answer")
for i in answer_list:
    print(" ".join(map(str, i)))
    
    
    

