# # # # # # # # # for i in range(1, 6):
# # # # # # # # #     print(i)

# # # # # # # # i = 0
# # # # # # # # while(i<3):
# # # # # # # #     print(i)
# # # # # # # #     i= i + 1
# # # # # # # #     print("\n")
# # # # # # # #     print(i)
# # # # # # # # print(i)


# # # # # # # def avrage(*num):
# # # # # # #     print(type(num))
# # # # # # #     sum = 0
# # # # # # #     for i in num :
# # # # # # #         sum = sum + i
# # # # # # #     print("the sum is :", sum)
# # # # # # # avrage(4,5) #it will take the values as tuple and then sum it up

# # # # # # # def average1(**num):
# # # # # # #     print(type(num))  # it will print the type of num as dictionary
# # # # # # #     sum =0
# # # # # # #     for i in num:
# # # # # # #         sum = sum + num[i]
# # # # # # #     print("the sum is :",sum)
    
# # # # # # # average1(a=5,b=6)  


# # # # # # import welcome
# # # # # # welcome.wel()


# # # # # # with open("cons.txt","a") as f:
# # # # # #     f.writelines("This is a new second created by python")
# # # # # # with open("cons.txt","r") as re:
# # # # # #     while True:
# # # # # #         line = re.readline()
# # # # # #         if not line:
# # # # # #             break
# # # # # #         print(line)
        
        
# # # # # with open("yoyo.txt","w") as y:
# # # # #     i =1
# # # # #     while(i<11):
# # # # #         y.writelines(f"line {i}\n")
# # # # #         i = i + 1


# # # # square = lambda x : x**2
# # # # print(square(5)) 

# # # # table = lambda x,y:x*y
# # # # for i in range(1,11):
# # # #     print(f"5 x {i} =", table(5,i))
# # # #     i = i + 1
    
# # # # a = int(input("enter number value : "))
# # # # for i in range(1,11):  
# # # #     (lambda a,b : print(f"{a} * {b} = {a*b}"))(a,i)
# # # #     i = i + 1

# # # from functools import reduce
# # # l = [1,2,3,4,5,6]
# # # # squ = lambda x : x*x 
# # # # print(list(map(lambda x : x*x,l)))
# # # print(list(filter(lambda x: x>3,l)))
# # # print(reduce(lambda x,y : x+y,l))


# # class dog:
# #     name = "tommy"
# #     colour = "black"
# #     def info(self):
# #         print(f"the name of the dog is {self.name} and colour is {self.colour}")
        
    
# # a = dog()
# # b = dog()
# # b.name = "rock"
# # b.colour = "white"
# # a.info()
# # b.info()



# class myclass:
#     def __init__(self,value):
#         self.value = value
#     def pri(self):
#         print(f"value is {self.value}")
        
# a = myclass(2)
# a.pri()


class myclass:
    def __init__(self,value):
        self._value = value
        
    def show(self):
        print(f"value is {self._value}")
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,new_value):
        self._value = new_value

a = myclass(10)
a.show()
a.value = 5
a.show()
