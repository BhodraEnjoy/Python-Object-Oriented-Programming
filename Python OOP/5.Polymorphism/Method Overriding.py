class Father:
    def sleep(self):
        print("Sleep from 10:00 Pm to 5:00 Am ")
    def  eat(self):
        print("eating")

class Son(Father):
    def sleep(self):
        print("Sleep from 2:00 Am to 10:00 Am ")
        super().sleep()

ram = Son()
ram.sleep()

"""In Python, method overriding supports runtime polymorphism,
but method overloading does not support compile-time polymorphism
because Python is dynamically typed."""