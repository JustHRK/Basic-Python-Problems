#WAP to read a text from a given file "poem.txt" and find out whether it contains "twinkle"

f=open('poem.txt','r')
x=f.read()
print(x.find("twinkle"))
f.close()