import math
def triangle():
    a=int(input("Enter The value of A :"))
    b=int(input("Enter The value of B :"))
    c=int(input("Enter The value of C :"))
    if(a+b>c and b+c>a and c+a>b):
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of Triangle is=",area)
    else:
        print("<<<triangle is not possible>>>")
triangle()