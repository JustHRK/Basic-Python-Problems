#A file contains a word "donkey" multiple times you need to write a program which replaces this word by updating the same file.

with open("donkey.txt","r") as f:
    x=f.read()
x=x.replace("donkey","######")
with open("donkey.txt","w") as f:    
    f.write(x)

    