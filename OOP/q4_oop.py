#Add a static method in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self):
        self.num=int(input("Enter a Number: "))
        print("""Choose Operation:
        1. Square
        2. Cube
        3. Square Root""")
        self.op=int(input("Operation: "))

    def getResult(self):
        if(self.op==1):
            print("Square= ",self.num**2)
        elif(self.op==2):
            print("Cube= ",self.num**3)
        elif(self.op==3):
            print("Square= ",self.num**0.5)    
    
    @staticmethod
    def greet():
        print("Hello User!")

n1=Calculator()
n1.greet()
n1.getResult()