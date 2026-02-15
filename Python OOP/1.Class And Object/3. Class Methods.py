class Instructor: 
    followers=0 #Class object variable
    def __init__(self,instructor_name,address):
        self.name = instructor_name
        self.address = address
    #    self.followers = 1000
    def display(self,suject_name):
        print(f"Hi, i am {self.name} and i teach {suject_name}")



instructor = Instructor("Enjoy","China") 
print(instructor.name)
instructor.display("Python")
print(instructor.followers)