"""Multlevel Inheritance in Python"""
class Human(object):
    def  __init__(self, num_heart):
        print("Calling init of Human class")
        self.num_eyes = 2
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name):
        print("Calling init of Male class")
        self.name = name
    def Sleep(self):
        print("I can Sleep Whole day")
class Boy(Male):
    def __init__(self,name ,can_dacne,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.can_dance = can_dacne
    def work(self):
       # Human.work(self)
        super().work()
        print("I can Code")
class Programmer(Boy):
    def work(self):
        super().work()
        print("I can write Program")
boy_1 = Boy("Rahul",True,1)
print(boy_1.name)
print(boy_1.can_dance)
print(boy_1.num_eyes)
print(boy_1.num_heart)
print(Boy.mro())
#boy_1.eat()
#boy_1.work()
#programmer_1 = Programmer()
#programmer_1.eat()
#programmer_1.work()
