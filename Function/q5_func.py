#WAP using function to print first n line of the following pattern
# * * *
# * *
# *

from re import I


n=int(input("enter a num: "))

def pattern(n):
    for i in range(n):
        print("* "*(n-i))

pattern(n)
