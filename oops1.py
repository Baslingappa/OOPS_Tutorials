#Initiating a class
class Employee:
    #Special fun/method, Magic methods,Dunder method/Constructor
    def __init__(self):
        self.Salary=50000
        self.ID=23
        self.Designation="Staff software engineer"

#Creating an Obj of a class
sam=Employee()
print(sam.ID)
print(sam.Designation)
print(sam.Salary)