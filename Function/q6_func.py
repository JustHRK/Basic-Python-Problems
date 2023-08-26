#WAP using function to convert inches to centimeter

x=float(input("Enter len in inches: "))

def convert(x):
    return (x*2.54)

print(x, " in cms: ",convert(x))