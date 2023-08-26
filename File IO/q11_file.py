#WAP to rename a file to "renamed_by_python.txt"

import os
oldName="rename.txt"
newName="renamed_by_python.txt"
with open(oldName) as f:
    x=f.read()
with open(newName,"w") as f2:
    f2.write(x)
os.remove(oldName)