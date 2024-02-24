# single inheritance
"""
class math:
    def add(self,x,y):
        return x+y
class inheritance(math):
    def sub(self,x,y):
        return x-y
p=inheritance()
a=p.add(4,2)                 
print("x+y=",a)
b=p.sub(12,4)
print("x-y=",b)
                                   
"""
class math:
    def add(self,x,y):
        return x+y
class inheritance(math):
    def sub(self,x,y):
        return x-y
p=inheritance()
a=p.add(10,5)
print("x+y=",a)
b=p.sub(40,20)
print("x-y=",b)

#multilavel inheritance..

class math1:
    def add(self,a,b):
        return a+b
class minuse(math1):
    def sub(self,a,b):
        return a-b
class multii(minuse):
    def multi(self,a,b):
        return a*b
p=multii()
a=p.add(40,30)
print("a+b= ",a)
b=p.sub(50,30)
print("a-b= ",b) 
c=p.multi(5,6)
print("a*b= ",c)