#WAP to find whether a given name is present in list or not

nameList=["harshal","prathamesh","ayush", "anuj"]
name=input("enter name:")
if(name in nameList):
    print("Available")
else:
    print("Unavailable")
