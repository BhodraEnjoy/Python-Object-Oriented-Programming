#print(1+2)
#print('1'+'2')
#print(int.__add__(1,2))
#print(str.__add__('1','2'))

class ComplexNumber:
    def __init__(self,real,imaginary ):
        self.real = real
        self.imaginary = imaginary 
    def __add__(self,other):
        #return f"{self.real+other.real}+{ self.imaginary+other.imaginary}i"
        return str(self.real+other.real)+ "+" + str(self.imaginary+other.imaginary) + "i"

c1 = ComplexNumber(1,2)
c2 = ComplexNumber(4,5)
print(c1+c2)

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __gt__(self,other): #__gt__ grater then #__lt__ less then
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("Enjoy",23)
p2 = Person("Bhodra",22)

if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")

