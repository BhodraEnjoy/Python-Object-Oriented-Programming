# list1= [1,2,3,4]

# for i in list1:
#     print(i)
# print(len(list1))
# print(list1)
# print(8+9)
# print(dir(int))
class Author:
    def __init__(self,name,book_name,pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    def __call__(self, *args, **kwds):
        print("Hi")
    def __del__(self):
        print("Suthor object has been deleted")

d = Author("Enjoy","Python",522)
print(len(d))
print(str(d))
d()
del d
print(d)