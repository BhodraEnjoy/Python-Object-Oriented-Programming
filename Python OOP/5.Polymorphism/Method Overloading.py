class Demo:
#    def add(self,a,b):
#        return a + b
#    def add(self,a,b,c=0):
#        return a + b + c
    
    def add(self,*args):
        total = 0
        for i in args:
            total+=i
        return total

d = Demo()
print(d.add(2,3))
print(d.add(1,2,3))
print(d.add(1,2,3,4,5,6,7,8,9,10))