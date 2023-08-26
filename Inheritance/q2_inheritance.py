#Create a class Pets from a class Animals and further create Dog from Pets. Add a Method bark to Class Dog.

class Animals:
    animalType="Mammal"

class Pets(Animals):
    color="white"

class Dog(Pets): 
    @staticmethod
    def bark():
        print("BARK! BARK!") 
#OR
#class Dog(Pets): 
    # def bark(self):
    #     print("BARK! BARK!")

d=Dog()
d.bark()