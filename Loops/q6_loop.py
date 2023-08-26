#WAP to calculate factorial of a given number using for loop

from re import I


n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial:",fact)