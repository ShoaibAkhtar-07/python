# class employee:
#     def __init__(self):
#         print("constructor of employee")
#     a=1
# class programmer():
#     def __init__(self):
#         # super().__init__()
#         print("constructor of programmer")
#     b=2
# class manager(employee,programmer):
    
#     def __init__(self):
#         super().__init__()
#         print("constructor of manager")
#     c=3
        
# o=manager()
# print(o.a,o.b,o.c)

# 2 # DUCK TYPING
# class pycharm:
#     def execute(self):
#         print("running")
#         print("compiling")
        
# class vscode:
#     def execute(self):
#         print("running")
#         print("compiling")
#         print("edit")
#         print("debug")
        
# class laptop:
#     def code(self,ide):
#         ide.execute()
        
# ide = vscode()

# lap1 = laptop()
# lap1.code(ide)

# 3 
class std:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def __add__(self,other):
        p1= self.m1+other.m1
        p2= self.m2+other.m2
        s3 =std(p1,p2)
        return s3
    
    def __gt__(self,other):
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2
        if r1 > r2:
            return True
        else:
            return False
    
s1 = std(99,66)
s2 = std(45,54)
s3 = s1 + s2
print(s3.m1)

if s1 > s2 :
    print("s1 wins")
else:
    print("s2 wins")