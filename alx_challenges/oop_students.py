# this code is about the student section and i'm trying to integrate
#  oop using class, inheritance, methods and polymorphism

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def student_description(self):
        print (f"my name is {self.name} and i am {self.age} years old")

student1 = student("john", 26)
student1.student_description()
