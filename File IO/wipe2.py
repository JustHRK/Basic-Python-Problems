a = open("read.txt", 'r')
b= open ("write.txt",'w')
  
l=a.readlines()
z=len(l)

for i in range(1,z):
    k=a.readline()
    b.writeline(k)

a.close()
b.close()