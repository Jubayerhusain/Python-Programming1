def multiply(number):
    total=1
    for i in number:
        total*=i
    return total
print("The multiply is =",multiply((8,2,3,10,7)))