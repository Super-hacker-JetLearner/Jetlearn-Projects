
dictionary = {}
master_accounts = {"Super-Hacker-JetLearner": "im smarter than you"}

print("welcome to the username/password app!")

while True:
    print('1. add an account \n 2. sign in \n 3. print all')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        error = False
        stop = False
        count = 0
        while not stop and count < 4:
            new_username = input("Enter a username: ")
            if new_username not in dictionary:
                stop = True
            else:
                print("That username is already taken!")
                count += 1
        
        if count >= 4:
            error = True
            print("error")
        if not error:
            new_password = (input("Enter your password: "))
            # print("\033[F hello")

            print(f"\033[1AEnter your password: {"-" * len(new_password)}")
            
            dictionary[new_username] = new_password
        
        
    elif choice == "2":
        error = False
        stop = False
        count = 0
        while not stop and count < 4:
            sign_username = input("Enter your username: ")
            if sign_username in dictionary:
                stop = True
            else:
                print("that username does not exist!")
                count += 1
                
        if count >= 4:
            error = True
            print("error")
        if not error:
            stop = False
            count = 0
            while not stop and count < 4:
                sign_password = (input("Enter your password: "))
                print(f"\033[1AEnter your password: {"-" * len(sign_password)}")
                
                if dictionary[sign_username] == sign_password:
                    print("you are signed in!")
                    stop = True
                else:
                    print("that is the wrong password!")
                    count += 1
                    
            if count >= 4:
                print("error")
                
    elif choice == "3":
        error = False
        stop = False
        count = 0
        while not stop and count < 4:
            sign_username = input("Enter your master username: ")
            if sign_username in master_accounts:
                stop = True
            else:
                print("that username does not exist!")
                count += 1
                
        if count >= 4:
            error = True
            print("error")
        if not error:
            stop = False
            count = 0
            while not stop and count < 4:
                sign_password = (input("Enter your master password: "))
                print(f"\033[1AEnter your master password: {"-" * len(sign_password)}")
                
                if master_accounts[sign_username] == sign_password:
                    print("you are master signed in!")
                    stop = True
                else:
                    print("that is the wrong password!")
                    count += 1
                    
            if count >= 4:
                print("error")
        print(dictionary)
            