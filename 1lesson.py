class fruit():
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference
        
    def get_shape(self):
        return self.shape
    
    def set_shape(self, new_shape):
        self.shape = new_shape
        
    def increase_preference(self):
        self.preference += 1
        
    def show_fruit(self):
        print('This is a fruit of the color {}, the taste {}, the shape {}, and the preference {}'.format(self.color, self.taste, self.shape, self.preference))
        
        
    # def __getattribute__(self, name):
    #     if name == 'color':
    #         return object.__getattribute__(self, name)

        

# apple = fruit('red', 'sweet', 'round', 1)
# apple.show_fruit()

# apple.increase_preference()

# apple.show_fruit()

# apple.set_shape('sphere')

# apple.show_fruit()

# print(apple.get_shape())




# hidden attributes: start attribute name start with __






class User():
    def __init__(self, email, password):
        self.email = email
        self.__password = password
        
    def get_password(self):
        return self.__password
    
    def set_password(self):
        old_password = input('Enter your old password: ')
        if old_password == self.__password:
            new_password = input('Enter your new password: ')
            self.__password = new_password
            
        else:
            print('Wrong old password!')
            
    def show_account(self):
        print('Email: {}, password: {}'.format(self.email, self.__password))
        
        
        
# person = User('my email', 'my password')

# person.show_account()

# # person.set_password()

# print(person.get_password())



class Car():
    def __init__(self, brand, model, color, max_speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = max_speed
        
    def show_car(self):
        print('Brand: {}, model: {}, color: {}, max speed: {}'.format(self.brand, self.model, self.color, self.max_speed))
        
    

# audi = Car('Audi', 'some model', 'blue', '99999')

# audi.show_car()


class SUV(Car):
    def __init__(self, brand, model, color, max_speed, size):
        Car.__init__(self, brand, model, color, max_speed)
        self.size = size
        
    def show_car(self):
        print('Brand: {}, model: {}, color: {}, max speed: {}, size: {}'.format(self.brand, self.model, self.color, self.max_speed, self.size))
        
        

SUV_Audi = SUV('Audi', 'some model', 'white', '9999', 'very big')

SUV_Audi.show_car()



