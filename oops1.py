#Initiating a class
class Employee:
    #Special fun/method, Magic methods,Dunder method/Constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.Salary=50000
        self.ID=23
        self.Designation="Staff software engineer"
        print("attributes and data has been initiated")

    def Travel(self,Destination):
        print("This travel function/method is called manually")
        print(f"Employee is now travelling to {Destination}")

#Creating an Obj of a class
sam=Employee()
print(type(sam))
#sam.Travel("Kerala")
# print(sam.ID)
# print(sam.Designation)
# print(sam.Salary)
