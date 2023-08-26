#WAP to find out the line number where python is present for ques 6
x=True
i=1
with open("log.txt") as f:
    while(x):
        x=f.readline()
        i+=1
        if "python" in x:
            print(x)
            print("python:found")
            print("at:",i)
        