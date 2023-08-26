f1=open("read.txt","r")    
f2=open("write.txt","w")
l=f1.readlines()
z=len(l)
for i in range(0,z):
    f2.writelines(l[i])
f1.close()
f2.close()