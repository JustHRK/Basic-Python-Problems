#WAP to print multiplication table of a given number using  for loop

n=int(input("Enter a Number:"))
for i in range(1,11):
    print("%d x %d = %d " %(n,i,n*i))