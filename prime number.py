
"""
    def prime(n):
        if(n==1):
            return False
        elif(n==2):
            return True
        else:
            for i in range(2,n):
                if(n%i==0):
                    return False
            return True
    print(prime(int(input("Enter the value = "))))
"""
while(1):
    def prime ():
        n=int(input("value=" ))
        if(n==0  or n==1):
            print("not prime")
        else:
            for i in range(2,n):
                if(n%i==0):
                    print("not prime")
            print("prime")
    prime()
