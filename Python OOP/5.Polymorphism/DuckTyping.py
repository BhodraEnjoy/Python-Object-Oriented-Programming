class Duck:
    def swim(self):
        print("I am a duck and i am swim")
    def speaks(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a dog and i am swim")
    def speaks(self):
        print("woof woof")

class Person:
    def speaks(self):
        print("woof woof")

def dispaly(obj):
    obj.swim()
    obj.speaks()
    print("Information Dislplayed")
    
duck = Duck()
dispaly(duck)

dog =  Dog()
dispaly(dog)

person = Person()
dispaly(person)