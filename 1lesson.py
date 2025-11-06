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

        

apple = fruit('red', 'sweet', 'round', 1)
apple.show_fruit()

apple.increase_preference()

apple.show_fruit()

apple.set_shape('sphere')

apple.show_fruit()

print(apple.get_shape())



