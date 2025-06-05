dictionary = {}

print("welcome to dictionary")

while True:
    print('1. insert \n 2. display all countries \n 3. display all capitals \n 4. get capital \n 5. delete country \n 6. show dictionary')
    choice = input("enter your choice: ")
    
    if choice == "1":
        new_country = input("Enter the name of the country: ").upper()
        new_capital = input("Enter the name of the capital: ").upper()
        dictionary[new_country] = new_capital
        
    elif choice == "2":
        for k in dictionary:
            print(k)
            
    elif choice == "3":
        for i in dictionary:
            print(dictionary[i])
            
    elif choice == "4":
        get_country = input("Enter the name of the country: ").upper()
        get_capital = dictionary[get_country]
        print(get_capital)
        
    elif choice == "5":
        del_country = input("Enter the name of the country: ").upper()
        del dictionary[del_country]
        
    elif choice == "6":
        for i in dictionary:
            print(i, " : ", dictionary[i])
