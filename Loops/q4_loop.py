#WAP to check whether the number is prime or not...
 
from tkinter.tix import Tree


n=int(input("enter:"))
x=False
for i in range(2,n):
    if(n%i==0):
        x=True
        break
if(x):
    print("Not Prime")
else:
    print("Prime")