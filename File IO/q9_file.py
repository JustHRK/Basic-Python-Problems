#WAP to find out whether a file is identical and matches the content of another file

with open("this.txt") as f:
    x=f.read()
with open('that.txt') as f:
    y=f.read()

if x==y:
    print("Files are Identical")
else:
    print("Files aren't identical")