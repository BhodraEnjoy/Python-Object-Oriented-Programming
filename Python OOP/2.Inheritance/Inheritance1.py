"""Single Inheritance in Python"""
class Human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class  Male(Human):
    def __init__(self,name,num_heart):
        super().__init__(num_heart)
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can Code")
    def display(self):
        print(f"Name: {self.name}, Number of heart: {self.num_heart}")
male1 =  Male("Enjoy Bhodra",2)
male1.eat()
male1.work()
male1.flirt()
male1.display()
print(male1.num_eyes)
print(male1.name)
print(male1.num_heart)