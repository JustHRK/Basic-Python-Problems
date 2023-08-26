#WAP to find multiplication table of n using for loop in reverse order

n=int(input("Enter a num:"))
for i in range(0,10):
    print(f"{n}x{10-i}={n*(10-i)}")