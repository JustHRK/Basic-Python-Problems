#Create a class C2dVector and use it to create another class representing 3-dVector.

class C2dVector:
    def __init__(self,i , j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"(i,j)=( {self.icap}, {self.jcap})"

class C3dVector(C2dVector):
    def __init__(self,i , j, k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"(i,j,k)=( {self.icap}, {self.jcap}, {self.kcap})"

v2d=C2dVector(3,5)
v3d=C3dVector(6,8,10)
print (v2d)
print (v3d)