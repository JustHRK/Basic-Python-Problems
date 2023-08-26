#Create a class programmer for storing information of few programmers working at Microsoft

class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position

    def getinfo(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print("Postion: ",self.position)

emp1=Programmer("Harshal","35 LPA","Senior Developer")
emp2=Programmer("Prathamesh","12 LPA","Intern")
emp1.getinfo()
emp2.getinfo()