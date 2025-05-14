
# # PROBLEM 1

# class twoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#             print(f"the vector is {self.i}i + {self.j}j")
            
        
    
# class threeDvector(twoDvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#             print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

    
# a=twoDvector(1,2)
# a.show()
# b=threeDvector(1,2,3)
# b.show()

# # PROBLEM 2

# class animals:
#     pass
# class pets(animals):
#     pass
# class dog(pets):
#     def bark(self):
#         print("~~bow bow~~")
        
# a = dog()
# a.bark()

# # PROBLEM 3

# class employee:
#     salary=99999
#     increment=50
#     @property
#     def totalsalaryafterincrement(self):
#         return (self.salary * (1+(self.increment/100)))
#     @property
#     def salaryafterincrement(self):
#         return self.salary * (self.increment/100)
        

# e = employee()

# print(f"TOTAL salary after increment = {e.totalsalaryafterincrement}")
# print(f"Incremented amount = {e.salaryafterincrement}")

# PROBLEM 4

class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,s2):
        return complex(self.a+s2.a,self.b+s2.b)
    def __str__(self):
        return f"{self.a}+{self.b}"

        
s1 = complex(1,2)
s2 = complex(3,4)
print(s1+s2)