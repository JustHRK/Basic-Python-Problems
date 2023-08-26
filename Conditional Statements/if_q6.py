#WAP to calculate grade of a student from his marks 

marks=int(input("Enter Your marks:"))
if(marks>=90 and marks<=100):
    print("Grade: Excellent")
elif(marks>=80):
    print("Grade: A")
elif(marks>=70):
    print("Grade: B")    
elif(marks>=60):
    print("Grade: C")
elif(marks>=50):
    print("Grade: D")
else:
    print("Grade: F")