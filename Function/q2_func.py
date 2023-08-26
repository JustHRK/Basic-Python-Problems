#WAP using function to convert celsius to fahrenheit

c=float(input("Enter temp in celsius: "))

def convert(c):
    f=32+((9*c)/5)
    return f

print ("Temp in Fahrenheit: ",convert(c))