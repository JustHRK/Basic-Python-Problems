#Create a class Employee and add Salary and Increment properties to it.Write a Method salaryAfterIncrement with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary=5000
    increment=1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,val):
        self.increment=val/self.salary

e1=Employee()
print(e1.increment)
print(e1.salaryAfterIncrement)
e1.salaryAfterIncrement=10000
print(e1.increment)