# ## WALRUS OPERATOR

# data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# results = [n for n in data if n > 5]
# print(results)

# data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print([n for n in data if (x := n) > 5])



# # 2

# if(value := len("shoaib akhtar"))>0:
#     print(value)
    
# if (value := len("shoaib akhtar") - "shoaib akhtar".count(" ")) > 0:
#     print(value)



# # 3

# while(n:=input("enter : "))!="quit":
#     print(n)                           
# # n = input("enter :")
# # while(n != "quit"):
# #   print(f"you entered {n}")
# #   n = input("enter :")
  
   
   
# # 4
# results = [y for x in range(1,10) if (y := x**2) > 10]
# print(results)


   
# 5

n = [1,4,2,3,5,6,7]
while (n := len(n)) > 0:
    print(n.pop())