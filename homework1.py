

class person():
    def __init__(self, name, age, country_of_origin):
        self.name = name
        self.age = age
        self.country_of_origin = country_of_origin
    def show(self):
        print('name: {}, age: {}, country: {}'.format(self.name, self.age, self.country_of_origin))
        
    
    
class student(person):
    def __init__(self, name, age, country_of_origin, school, class_name):
        super().__init__(name, age, country_of_origin)
        self.school = school
        self.class_name = class_name
        
    def show(self):
        print('name: {}, age: {}, country: {}, school: {}, class: {}'.format(self.name, self.age, self.country_of_origin, self.school, self.class_name))
        
        

me = student('Bartosz', 12, 'Poland', 'AICS', 'MYP2E')
me.show()

