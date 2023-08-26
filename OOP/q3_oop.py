#Create a class with class attribute a,create an object from it and set a directly using object.a=0.Does this change the class attrribute?

class Cls:
    a=10

object=Cls()
object.a=0
print(object.a)
print(Cls.a)

#No, "object.a=0" only changes value of a for that object and not for the clas attribute.
