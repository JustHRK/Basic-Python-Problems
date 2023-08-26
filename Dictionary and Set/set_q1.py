#WAP to input eight numbers from the user and display all the unique numbers

s=set()
for i in range (0,8):
    x=int(input("Enter number:"))
    s.add(x)
print(s)