class Student:
    def __init__(self,name):
        self.name=name#to hold current object
    def greet(self):
        print(f"Welcome to python workshop {self.name}")
        
s1=Student("Anu")
s2=Student("Dinesh")

s1.greet()
s2.greet()                