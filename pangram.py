dictionary = {}
for i in range (65, 91):

    dictionary[chr(i)] = 0

text = input("Enter a string: ").upper()

def check_pangram(dict):
    for i in dict:
        if dict[i] == 0:
            return False
    return True

for i in text:
    if i in dictionary:

        old = dictionary[i]
        old += 1
        dictionary[i] = old

if check_pangram(dictionary):
    print("this is a pangram")
else:
    print("this is not a pangram")

