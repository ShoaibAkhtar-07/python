class employee:
    def __init__(self):
        print("constructor of employee")
    a=1
class programmer(employee):
    def __init__(self):
        super().__init__()
        print("constructor of programmer")
    b=2
class manager(programmer):
    
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c=3
        
o=manager()
print(o.c)