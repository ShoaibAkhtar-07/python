# # # # # # # # # # # # # # # # # # for i in range(1, 6):
# # # # # # # # # # # # # # # # # #     print(i)

# # # # # # # # # # # # # # # # # i = 0
# # # # # # # # # # # # # # # # # while(i<3):
# # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # #     i= i + 1
# # # # # # # # # # # # # # # # #     print("\n")
# # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # print(i)


# # # # # # # # # # # # # # # # def avrage(*num):
# # # # # # # # # # # # # # # #     print(type(num))
# # # # # # # # # # # # # # # #     sum = 0
# # # # # # # # # # # # # # # #     for i in num :
# # # # # # # # # # # # # # # #         sum = sum + i
# # # # # # # # # # # # # # # #     print("the sum is :", sum)
# # # # # # # # # # # # # # # # avrage(4,5) #it will take the values as tuple and then sum it up

# # # # # # # # # # # # # # # # def average1(**num):
# # # # # # # # # # # # # # # #     print(type(num))  # it will print the type of num as dictionary
# # # # # # # # # # # # # # # #     sum =0
# # # # # # # # # # # # # # # #     for i in num:
# # # # # # # # # # # # # # # #         sum = sum + num[i]
# # # # # # # # # # # # # # # #     print("the sum is :",sum)
# # # # # # # # # # # # # # # # # # while(i<3):
# # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # #     i= i + 1
# # # # # # # # # # # # # # # # # #     print("\n")
# # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # print(i)
# # # # # # # # # # # # # # # # #     for i in num :
# # # # # # # # # # # # # # # # #         sum = sum + i
# # # # # # # # # # # # # # # # #     print("the sum is :", sum)
# # # # # # # # # # # # # # # # # def average1(**num):
# # # # # # # # # # # # # # # # #     print(type(num))  # it will print the type of num as dictionary
# # # # # # # # # # # # # # # # #     sum =0
# # # # # # # # # # # # # # # # #     for i in num:
# # # # # # # # # # # # # # # # #         sum = sum + num[i]
# # # # # # # # # # # # # # # # #     print("the sum is :",sum)
    
# # # # # # # # # # # # # # # # average1(a=5,b=6)  
# # # # # # # # # # # # # # # # # average1(a=5,b=6)  


# # # # # # # # # # # # # # # import welcome
# # # # # # # # # # # # # # # welcome.wel()

# # # # # # # # # # # # # # # # import welcome
# # # # # # # # # # # # # # # # welcome.wel()

# # # # # # # # # # # # # # # with open("cons.txt","a") as f:
# # # # # # # # # # # # # # #     f.writelines("This is a new second created by python")
# # # # # # # # # # # # # # # with open("cons.txt","r") as re:
# # # # # # # # # # # # # # #     while True:
# # # # # # # # # # # # # # #         line = re.readline()
# # # # # # # # # # # # # # #         if not line:
# # # # # # # # # # # # # # #             break
# # # # # # # # # # # # # # #         print(line)

# # # # # # # # # # # # # # # # with open("cons.txt","a") as f:
# # # # # # # # # # # # # # # #     f.writelines("This is a new second created by python")
# # # # # # # # # # # # # # # # with open("cons.txt","r") as re:
# # # # # # # # # # # # # # # #     while True:
# # # # # # # # # # # # # # # #         line = re.readline()
# # # # # # # # # # # # # # # #         if not line:
# # # # # # # # # # # # # # # #             break
# # # # # # # # # # # # # # # #         print(line)
        
        
# # # # # # # # # # # # # # with open("yoyo.txt","w") as y:
# # # # # # # # # # # # # #     i =1
# # # # # # # # # # # # # #     while(i<11):
# # # # # # # # # # # # # #         y.writelines(f"line {i}\n")
# # # # # # # # # # # # # #         i = i + 1
# # # # # # # # # # # # # # # with open("yoyo.txt","w") as y:
# # # # # # # # # # # # # # #     i =1
# # # # # # # # # # # # # # #     while(i<11):
# # # # # # # # # # # # # # #         y.writelines(f"line {i}\n")
# # # # # # # # # # # # # # #         i = i + 1


# # # # # # # # # # # # # square = lambda x : x**2
# # # # # # # # # # # # # print(square(5)) 
# # # # # # # # # # # # # # square = lambda x : x**2
# # # # # # # # # # # # # # print(square(5)) 

# # # # # # # # # # # # # table = lambda x,y:x*y
# # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # #     print(f"5 x {i} =", table(5,i))
# # # # # # # # # # # # #     i = i + 1
# # # # # # # # # # # # # # table = lambda x,y:x*y
# # # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # # #     print(f"5 x {i} =", table(5,i))
# # # # # # # # # # # # # #     i = i + 1
    
# # # # # # # # # # # # # a = int(input("enter number value : "))
# # # # # # # # # # # # # for i in range(1,11):  
# # # # # # # # # # # # #     (lambda a,b : print(f"{a} * {b} = {a*b}"))(a,i)
# # # # # # # # # # # # #     i = i + 1

# # # # # # # # # # # # from functools import reduce
# # # # # # # # # # # # l = [1,2,3,4,5,6]
# # # # # # # # # # # # # squ = lambda x : x*x 
# # # # # # # # # # # # # print(list(map(lambda x : x*x,l)))
# # # # # # # # # # # # print(list(filter(lambda x: x>3,l)))
# # # # # # # # # # # # print(reduce(lambda x,y : x+y,l))

# # # # # # # # # # # # # # for i in range(1,11):  
# # # # # # # # # # # # # #     (lambda a,b : print(f"{a} * {b} = {a*b}"))(a,i)

# # # # # # # # # # # # # from functools import reduce
# # # # # # # # # # # # # l = [1,2,3,4,5,6]
# # # # # # # # # # # # # # squ = lambda x : x*x 
# # # # # # # # # # # # # # print(list(map(lambda x : x*x,l)))
# # # # # # # # # # # # # print(list(filter(lambda x: x>3,l)))
# # # # # # # # # # # # # print(reduce(lambda x,y : x+y,l))

# # # # # # # # # # # class dog:
# # # # # # # # # # #     name = "tommy"
# # # # # # # # # # #     colour = "black"
# # # # # # # # # # #     def info(self):
# # # # # # # # # # #         print(f"the name of the dog is {self.name} and colour is {self.colour}")

# # # # # # # # # # # # # OOPS 

# # # # # # # # # # # # class dog:
# # # # # # # # # # # #     name = "tommy"
# # # # # # # # # # # #     colour = "black"
# # # # # # # # # # # #     def info(self):
# # # # # # # # # # # #         print(f"the name of the dog is {self.name} and colour is {self.colour}")
        
    
# # # # # # # # # # # a = dog()
# # # # # # # # # # # b = dog()
# # # # # # # # # # # b.name = "rock"
# # # # # # # # # # # b.colour = "white"
# # # # # # # # # # # a.info()
# # # # # # # # # # # b.info()
# # # # # # # # # # # # a = dog()
# # # # # # # # # # # # b = dog()
# # # # # # # # # # # # b.name = "rock"
# # # # # # # # # # # # b.colour = "white"
# # # # # # # # # # # # a.info()
# # # # # # # # # # # # b.info()



# # # # # # # # # # class myclass:
# # # # # # # # # #     def __init__(self,value):
# # # # # # # # # #         self.value = value
# # # # # # # # # #     def pri(self):
# # # # # # # # # #         print(f"value is {self.value}")
# # # # # # # # # # #     def __init__(self,value):
# # # # # # # # # # #         self.value = value
# # # # # # # # # # #     def pri(self):
# # # # # # # # # # #         print(f"value is {self.value}")
        
# # # # # # # # # # a = myclass(2)
# # # # # # # # # # a.pri()
# # # # # # # # # # # a = myclass(2)
# # # # # # # # # # # a.pri()



# # # # # # # # # # # gettter and setter

# # # # # # # # # class myclass:
# # # # # # # # #     def __init__(self,value):
# # # # # # # # #         self._value = value
# # # # # # # # # # class myclass:
# # # # # # # # # #     def __init__(self,value):
# # # # # # # # # #         self._value = value
        
# # # # # # # # #     def show(self):
# # # # # # # # #         print(f"value is {self._value}")
# # # # # # # # # #     def show(self):
# # # # # # # # # #         print(f"value is {self._value}")
        
# # # # # # # # #     @property
# # # # # # # # #     def value(self):
# # # # # # # # #         return self._value
# # # # # # # # # #     @property
# # # # # # # # # #     def value(self):
# # # # # # # # # #         return self._value
    
# # # # # # # # #     @value.setter
# # # # # # # # #     def value(self,new_value):
# # # # # # # # #         self._value = new_value
# # # # # # # # # #     @value.setter
# # # # # # # # # #     def value(self,new_value):
# # # # # # # # # #         self._value = new_value

# # # # # # # # # a = myclass(10)
# # # # # # # # # a.show()
# # # # # # # # # a.value = 5
# # # # # # # # # a.show()
# # # # # # # # # # a = myclass(10)
# # # # # # # # # # a.show()
# # # # # # # # # # a.value = 5
# # # # # # # # # # a.show()



# # # # # # # # # class and instance variables
# # # # # # # # # # class and instance variables

# # # # # # # # class employee:
# # # # # # # #     company_name = "ISRO"
# # # # # # # #     def __init__(self,name):
# # # # # # # #         self.name = name
# # # # # # # #         self.salary = "2cr"
# # # # # # # # # class employee:
# # # # # # # # #     company_name = "ISRO"
# # # # # # # # #     def __init__(self,name):
# # # # # # # # #         self.name = name
# # # # # # # # #         self.salary = "2cr"
        
# # # # # # # #     def showdetails(self):
# # # # # # # #         print(f"the name of the employee is {self.name} working in {self.company_name} with the  salary of {self.salary}")
# # # # # # # # #     def showdetails(self):
# # # # # # # # #         print(f"the name of the employee is {self.name} working in {self.company_name} with the  salary of {self.salary}")
        
    
    
# # # # # # # # emp1 = employee("shoaib")
# # # # # # # # # emp1.showdetails()
# # # # # # # # emp1.salary = "5cr"
# # # # # # # # emp1.company_name = "NASA"
# # # # # # # # employee.showdetails(emp1)
# # # # # # # # # emp1 = employee("shoaib")
# # # # # # # # # # emp1.showdetails()
# # # # # # # # # emp1.salary = "5cr"
# # # # # # # # # emp1.company_name = "NASA"
# # # # # # # # # employee.showdetails(emp1)

# # # # # # # # employee.company_name = "SPACE x"
# # # # # # # # print(employee.company_name)
# # # # # # # # # employee.company_name = "SPACE x"
# # # # # # # # # print(employee.company_name)

# # # # # # # # emp2 = employee("sarhan")
# # # # # # # # emp2.showdetails()
# # # # # # # # # emp2 = employee("sarhan")
# # # # # # # # # emp2.showdetails()
 

# # # # # # # # class method
# # # # # # # # # class method

# # # # # # # class employee:
# # # # # # #     company = "GOOGLE"
# # # # # # #     def __init__(self,name):
# # # # # # #         self.name = name
# # # # # # #     def show(self):
# # # # # # #         print(f"the name of the employee is {self.name} and company  is {self.company}")
# # # # # # # # class employee:
# # # # # # # #     company = "GOOGLE"
# # # # # # # #     def __init__(self,name):
# # # # # # # #         self.name = name
# # # # # # # #     def show(self):
# # # # # # # #         print(f"the name of the employee is {self.name} and company  is {self.company}")
        
# # # # # # #     @classmethod
# # # # # # #     def changecom(cls,new_comp):
# # # # # # #         cls.company = new_comp
# # # # # # # #     @classmethod
# # # # # # # #     def changecom(cls,new_comp):
# # # # # # # #         cls.company = new_comp
        
# # # # # # # e1 = employee("ravi")
# # # # # # # e1.show()
# # # # # # # e1.changecom("AMAZON")
# # # # # # # e1.show()
# # # # # # # print(employee.company)
# # # # # # # # e1 = employee("ravi")
# # # # # # # # e1.show()
# # # # # # # # e1.changecom("AMAZON")
# # # # # # # # e1.show()
# # # # # # # # print(employee.company)
    
    
    
# # # # # # # class methods as alternative constructors
# # # # # # # # class methods as alternative constructors

# # # # # # class employee:
# # # # # # # class employee:
    
# # # # # #     def __init__(self,name,salary):
# # # # # #         self.name = name
# # # # # #         self.salary = salary
# # # # # # #     def __init__(self,name,salary):
# # # # # # #         self.name = name
# # # # # # #         self.salary = salary
        
# # # # # #     @classmethod
# # # # # #     def fromstr(cls,string):
# # # # # #         return cls(string.split("-")[0],string.split("-")[1])
# # # # # # #     @classmethod
# # # # # # #     def fromstr(cls,string):
# # # # # # #         return cls(string.split("-")[0],string.split("-")[1])
    
    
# # # # # # e1 = employee("shoaib","5cr")
# # # # # # print(e1.name)
# # # # # # print(e1.salary)
# # # # # # # e1 = employee("shoaib","5cr")
# # # # # # # print(e1.name)
# # # # # # # print(e1.salary)

# # # # # # string = "ravi - 3cr"
# # # # # # e2 = employee.fromstr(string)
# # # # # # print(e2.name)
# # # # # # print(e2.salary)
# # # # # # # e2 = employee.fromstr(string)
# # # # # # # print(e2.name)
# # # # # # # print(e2.salary)

         
# # # # # # # SUPER KEYWORD

# # # # # # class father:
# # # # # #     def parent_cls(self):
# # # # # #         print("i am father class")
        
# # # # # # class child(father):
# # # # # #     def parent_cls(self):
# # # # # #         print("_sh0aib_akhtar")
# # # # # #         super().parent_cls()
        
# # # # # #     def child_cls(self):
# # # # # #         print("i am child")  
# # # # # #         super().parent_cls()
# # # # # # # e1 = father()
# # # # # # # e1.parent_cls()
# # # # # # e2 = child()
# # # # # # e2.child_cls()
# # # # # # e2.parent_cls()


# # # # # # # dunder
# # # # # class dunderstudent:
# # # # #     def __init__(self,name):
# # # # #         self.name = name
# # # # #     def __len__(self):
# # # # #         i = 0
# # # # #         for n in self.name:
# # # # #             i = i + 1
# # # # #         return i
# # # # #     def __str__(self):
# # # # #         return f"the name of the student is {self.name}"
# # # # #     def __repr__(self):
# # # # #         return f"this is not good to use repr to complete work but its OK {self.name}"
# # # # #     def __call__(self):
# # # # #         print(" hey! you can call me by call method")
            
        


# # # # # # # s1 = dunderstudent("shoaib")
# # # # # # # print(s1.name)
# # # # # # # print(len(s1))



# # # #  method overriding

# # # class square:
# # #     def __init__(self,x,y):
# # #         self.x=x
# # #         self.y=y
# # #     def area(self):
# # #         return self.x * self.y

# # # class circle(square):
# # #     def __init__(self,radius):
# # #         self.radius=radius
# # #         super().__init__(radius,radius)
        
# # #     def area(self):
# # #         return 3.14*super().area()
    
    
# # # v = square(2,3)
# # # print(v.area())

# # # s = circle(5)
# # # print(s.area())



# # #  operator overriding

# # class vector:
# #     def __init__(self,x,y,z):
# #         self.x = x
# #         self.y= y
# #         self.z = z
        
# #     def __str__(self):
# #         return (f"{self.x}i +{self.y}j + {self.z}k")
# #     def __add__(self,n):
# #         return vector(self.x + n.x , self.y + n.y , self.z + n.z)
    
    
# # v1 = vector(1,2,3)
# # print(v1)
# # v2 = vector(4,5,6)
# # print(v2)

# # print(v1 + v2)
# # print(type(v1 + v2))


# # single inheritance

# class animal:
#     def __init__(self,name,colour):
#         self.name = name
#         self.colour = colour
        
#     def animal_details(self):
#         print(f"the animal is {self.name} and it is {self.colour} in colour")
        
# class cat(animal):
#     def __init__(self,age,nick_name,animal_obj):
#         super().__init__(animal_obj.name,animal_obj.colour)
#         self.age = age
#         self.nick_name = nick_name
        
#     def cat_details(self):
#         print(f"the animal is {self.name}, it is {self.colour} in colour and it is {self.age} years old and it name is {self.nick_name}")


# ani1 = animal("cat","white")
# ani1.animal_details()

# ca = cat(3,"mickey",ani1)
# ca.cat_details()


# multiple inheritance

class student:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name of the student is {self.name}")
        
class skill:
    def __init__(self,language):
        self.language = language
    def show(self):
        print(f"The programing language which i know {self.language}")
        
class stuskill(skill,student):
    def __init__(self,name,language):
        self.name = name
        self.language = language

s1 = stuskill("shoaib"," C,PYTHON")
s1.show()
print(stuskill.mro())
        
        
    
        