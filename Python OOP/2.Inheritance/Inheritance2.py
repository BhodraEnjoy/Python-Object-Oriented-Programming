"""Mutiple Inheritance in Python"""
class Human:
    def __init__(self,num_heart):
        print("calling init of Human class")
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name):
        print("calling init of Male class")
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can Code")
    
class Boy(Human,Male):
    def __init__(self,name,language,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.language = language
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("i can test")
    def display(self):
        print(f"Name: {self.name}, Number of heart: {self.num_heart}, Language: {self.language}")

boy = Boy("Enjoy Bhodra","Python",1) 
print(boy.num_nose)
boy.display()
#print(boy.name)
#boy.eat()
#boy.flirt()
#boy.work()
#Male.work(boy)
#print(Boy.mro())