#WAP to accept marks of and display them in sorted manner

marks=[]

for i in range (0,6):
    marks.append(int(input("Enter Marks:")))
marks.sort()
print(marks)
