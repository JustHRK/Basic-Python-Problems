#WAP to make a copy of a file named "this.txt"

with open("this.txt") as f:
    x=f.read()

with open("that.txt","w") as f:
    f.write(x)
