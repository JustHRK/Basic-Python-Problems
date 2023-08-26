# WAP to find the greatest of four numbers entered by the user

a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
d=int(input("enter number 4:"))

if(a>b and a>c):
    if(a>d):
        print(a)
    else:
        print(d)
elif(b>a and b>c):
    if(b>d):
        print(b)
    else:
        print(d)
elif(c>a and c>b):
    if(c>d):
        print(c)
    else:
        print(d)                
