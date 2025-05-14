
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

# # PROBLEM 4

# class complex:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,s2):
#         return complex(self.a+s2.a,self.b+s2.b)
#     def __str__(self):
#         return f"{self.a}+{self.b}"

        
# s1 = complex(1,2)
# s2 = complex(3,4)
# print(s1+s2)

# PROBLEM 5

class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __add__(self,other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z *other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
        

        
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)

print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)
