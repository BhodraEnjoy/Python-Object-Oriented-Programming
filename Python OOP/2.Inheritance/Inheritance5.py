"""Hybrid Inheritance: When a class is derived from more than one base class, 
it is called hybrid inheritance. It combines the features of multiple inheritance and multilevel inheritance."""

class A:
    def display(self):
        print("Display from A class")
class B(A):
    def display(self):
        print("Display from B class")
class C:
    def display(self):
        print("Hi from C class")
class D(B,C):
    def display(self):
        print("Display from D class")
d1 = D()
d1.display()
print(D.mro())