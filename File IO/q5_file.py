#Repaeat question 4 for a listof such words to be censored.

from ctypes.wintypes import WORD


list=["donkey","dumb","stupid"]
with open("cnsored.txt","r") as f:
    x=f.read()

for word in list:
    x=x.replace(word,"######")
    with open("cnsored.txt","w") as f:    
        f.write(x)

    