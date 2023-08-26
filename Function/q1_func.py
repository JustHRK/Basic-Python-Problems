#WAP using function to find greatest of 3 no.s

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))

def greatest(a,b,c):
    if(a>=b and a>=c):
        print("Greatest no.:",a)
    elif(b>=a and b>=c):
        print("Greatest no.:",b)
    else:
        print("Greatest no.:",c)
    
greatest(a,b,c)