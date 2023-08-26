#a spam comment is defined as a text containing following keywords:"make a lot of money","buy now","subscribe this","click this". WAP to detect these spams.

x=input("Enter the text comment:")
if("make a lot of money" in x):
    print("SPAM")
elif("buy now" in x):
    print("SPAM")
elif("subscribe this" in x):
    print("SPAM")
elif("click this" in x):
    print("SPAM")    
else:
    print("NOT SPAM")