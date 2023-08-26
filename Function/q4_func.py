#Write a recursive function to calculate the sum of first n natural numbers

import re


n=int(input("Enter a number: "))

def sum(n):
    if n==0:
        return 0
    else:
        return (n + sum(n-1))

print(sum(n))