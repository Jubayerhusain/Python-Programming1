import math
def triangle():
    a=float(input("Enter the value of a: "))
    b=float(input("Enter the value of b: "))
    c=float(input("Enter the value of c: "))
    if (a+b>c and a+c>b and c+b>a):
        s=a+b+c/2
        area= math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of traingla is= ",area)
    else:
        print("triangle is not possible...")
triangle()