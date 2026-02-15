"""public,Protected,private """
class Student:
    def __init__(self, name,roll_name,age):
        self.name = name # public Instance variable
        self._roll_name = roll_name # protected Instance variable
        self.__age = age ## private Instance variable

    def get_age(self):
        return  self.__age
    def set_age(self,age):
        if age < 0:
            print("Inavlid ")
        else:
            self.__age = age


    def __display(self):
        print(f"Hi myself {self.name} with roll name {self._roll_name} from student class")
    def dipalyPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My age is {self.__age}")


# def showData():
#    b1 = Branch("Enjoy",22)
#    print(b1.name)
#    print(b1._roll_name)

#showData()
s1 = Student(name="Enjoy",roll_name=2,age = 20)
print(s1.get_age())
s1.set_age(45)
print(s1.get_age())

