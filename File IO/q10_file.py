#WAP to wipe out content of a file

with open('wipe.txt'):
    pass

with open('wipe.txt',"w") as f:
    f.write("")