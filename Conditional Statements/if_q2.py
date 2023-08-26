#WAP to find out whether a student is pass or fail , if it requires total 40% and atleast 33% in each subject to pass.Assume 3 subjects and take marks as input from user.

s1=int(input("Enter Marks for subject 1:"))
s2=int(input("Enter Marks for subject 2:"))
s3=int(input("Enter Marks for subject 3:"))
total=(s1+s2+s3)/3
if(total>=40):
    if(s1>=33 and s2>=33 and s3>=33):
        print("You're Pass.")
    else:
        print("You're Fail.")
else:
    print("You're Fail.")