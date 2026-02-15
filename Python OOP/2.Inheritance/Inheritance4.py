"""Hierarchical Inheritance in Python"""
class Human:
    def __init__(self,name,age):
        print("Calling init of Human class")
        self.name = name
        self.age = age
    def show_detalis(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,m_name,age,location):
        print("Calling init of Male class")
        Human.__init__(self,m_name,age)
        self.location = location
    def sleep(self):
        print("I can sleep whole day")
class Female(Human):
    def __init__(self,f_name,age,can_dance):
        print("Calling init of Female class")
        Human.__init__(self,f_name,age)
        self.can_dance = can_dance
    def show_detalis(self):
       # Human.show_detalis(self)
        print(f"Name: {self.name}, Age: {self.age}, Can Dance: {self.can_dance}")   
    def work(self):
        print("I can code")
Female_1 = Female("Jiya",25,True)
Female_1.eat()
Female_1.show_detalis()
#print(Female_1.age)

#male_1 = Male("Rahul",25,"Delhi")
#print(Male.mro())
#male_1.sleep()
#male_1.eat()