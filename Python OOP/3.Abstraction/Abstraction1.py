from Demo_Abstraction0 import Vehicle

class Bike(Vehicle):
    def __init__(self,no_of_tyres,color):
        super().__init__(no_of_tyres)
        self.color = color
    def start(self):
        print("start with kick")
    def display(self):
        #return super().display()
        print(f"My color bike color is {self.color}")

class Scooty(Vehicle):
    def __init__(self,no_of_tyres):
        super().__init__(no_of_tyres)
    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self,no_of_tyres,no_of_gears):
        super().__init__(no_of_tyres)
        self.no_of_gears = 6
    def start(self):
        print("Start with key")
