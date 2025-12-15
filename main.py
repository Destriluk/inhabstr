class Person:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print("Hello my name is:",self.name)
    
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
    def showgrade(self):
        print("I am in grade",self.grade)     

s1 = Student("Mark",9)
s1.greet()
s1.showgrade()