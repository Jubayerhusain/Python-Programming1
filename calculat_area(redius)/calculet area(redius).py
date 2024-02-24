import math
def circle():
    r=int(input("Enter value of R :"))
    area=math.pi*r**2
    print(area)
circle()

#OR

import math
def calculet_area(radius):
    myarea=math.pi*radius**2
    return myarea
radius=calculet_area(int(input("Enter The Value Of Radiue :")))
print("The Area of Radius is :",radius)
calculet_area(radius)