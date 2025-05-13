import random

# # PROBLEM 1

# class programmer:
#     company="microsoft"
#     def __init__(self,name,salary,phno):
#         self.name=name
#         self.salary=salary
#         self.phno=phno
# s=programmer("shoaib akhtar",999999999,4341)
# print(s.company,s.name,s.salary,s.phno)

# # PROBLEM 2

# class calculator:
#     @staticmethod
#     def hello():
#         print("Hello")
#     def __init__(self,nu):
#         self.nu=nu
#         print("~~The SQUARE is~~" ,end="")
#         print(self.nu*self.nu)
#         print("~~The CUBE is~~",end="")
#         print(self.nu**3)
#         print("~~The SQUARE ROOT is~~",end="")
#         print(self.nu**0.5)

# calculator.hello()
# cal= calculator(2)

# PROBLEM 3

class train:
    def __init__(self,trainNo,fro,to):
        self.trainNo=trainNo
        self.fro= fro
        self.to=to 
    def book(self):
        print(f"the ticket is booked in train no : {self.trainNo} fromm {self.fro} to {self.to}")
    def getstatus(self):
        print(f"train {self.trainNo} is running on time")
    def getfare(self):
        print(f"ticket fare of train no :{self.trainNo} from { self.fro} to {self.to} is {random.randint(99,9999)}")
        
t = train(12345,"hyd","delhi")
t.book()
t.getstatus()
t.getfare()