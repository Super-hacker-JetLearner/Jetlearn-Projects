# dictionary = {}
# for i in range (65, 91):

#     dictionary[chr(i)] = 0

# text = input("Enter a string: ").upper()

# def check_pangram(dict):
#     for i in dict:
#         if dict[i] == 0:
#             return False
#     return True

# for i in text:
#     if i in dictionary:

#         old = dictionary[i]
#         old += 1
#         dictionary[i] = old

# if check_pangram(dictionary):
#     print("this is a pangram")
# else:
#     print("this is not a pangram")

def check_pangram(set):
    for i in range(65, 91):
        if chr(i) not in set:
            return False
    return True




my_set = set()


text = input("Enter a string: ").upper()
for i in text:
    # if i.isalpha() and i not in my_set:
    #     # print(i, "is added to the set")
    my_set.add(i)

if check_pangram(my_set):
    print("This is a pangram")
else:
    print("This is not a pangram")
