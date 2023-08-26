#WAP to print following star pattern 
#   *
#  ***
# *****

n=3
for i in range(n):
    print(" "*(n-1-i),end="")
    print("*" * (2*i +1), end="") 
    print(" "*(n-1-i))
        
    