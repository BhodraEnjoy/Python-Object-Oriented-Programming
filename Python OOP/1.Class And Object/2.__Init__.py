"""Example_1"""
class Instructor: 
    def __init__(self):
        print("Creating new object")

instructor = Instructor() 
instructor.name = "Enjoy"
instructor.address = "China"
print(instructor.name)

instructor2 = Instructor() 
instructor2.name = "Enjoy"
instructor2.address = "China"
print(instructor2.name)

"""Example_2"""
class Instructor: 
    def __init__(self,instructor_name,address):
        self.name = instructor_name
        self.address = address
        self.followers = 1000

        
instructor = Instructor("Enjoy","China") 

print(instructor.name)
print(instructor.followers)

