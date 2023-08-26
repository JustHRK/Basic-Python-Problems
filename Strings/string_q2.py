#Write a program to fill in a letter template given belpw with name and date.

letter='''Dear <|Name|>,
You're Selected!
<|Date|>'''
n=input("Enter Name:")
d=input("Enter Date:")
letter=letter.replace("<|Name|>",n)
letter=letter.replace("<|Date|>",d)
print(letter) 
