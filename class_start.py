

class student():
    name = ""
    age = 12
    teacher = "Sruthi"
    school = "JetLearn"
    class_name = ""
    
    
    
    def __init__(self, class_name="", teacher="", name="", age=0, school=""):

        # global dictionary
        print("Making new student!!!")
        self.class_name = class_name
        self.teacher = teacher
        self.name = name
        self.age = age
        self.school = school
        # dictionary = {"name":self.name, "age":self.age, "teacher":self.teacher,"school":self.school,"class name":self.class_name,}
    
    def show_details(self):
        print(f"Age: {self.age}")
        print(f"Teacher: {self.teacher}")
        print(f"School: {self.school}")
        print(f"Class name: {self.class_name}")
        print(f"Name: {self.name}")
        
    def change_details(self):
        # attribute = input("Enter the thing you want to change (name,age,teacher,school,class name): ")
        # attribute = dictionary[attribute]
        # print(f"Old value: {self.attribute}")
        # self.attribute = input("Enter the new value: ")

        self.name = input("enter the new name: ")
        self.age = int(input("enter the new age: "))
        # self.teacher = int(input("enter the new teacher: "))
        # self.school = int(input("enter the new school: "))
        # self.class_name = int(input("enter the new class name: "))
        
        

student1 = student(class_name="my class",teacher="my teacher", name="somebody", age=14, school="no school")
student1.show_details()
student1.change_details()
student1.show_details()


# student1 = student("my class","my teacher")
# student1.show_details()
# student1.change_details()
# student1.show_details()