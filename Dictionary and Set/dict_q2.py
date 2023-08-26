#Create an empty dictionary.Allow 4 friends to enter their favourite language as values and use their names as keys assuming all have unique names

lang={}
for i in range(0,4):
    k=input("Enter Your name:")
    v=input("Enter your fav Language:")
    lang.update({k:v})
print(lang)
