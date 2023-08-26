#WAP to find sum of first n natural numbers using while loop

n=int(input("enter:"))
sum=0
while(n>=1):
    sum+=n
    n-=1
print("sum= ",sum)