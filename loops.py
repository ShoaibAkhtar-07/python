# # problem 1
# num = int(input("entre the num : "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# # problem 2
# l = ["shoaib","akhtar","sumaiya","sohail","zulekha"]
# for name in l:
#     if(name.startswith("s")):
#         print(f"helo {name}")

# # problem 3
# num = int(input("enter the num :"))
# for i in range(2, num):
#     if(num % i) == 0:
#         print("--this is not a prime number--")
#         break
# else:
#         print("--this is a prime number--")

# # problem 4
# num = int(input("enter the number : "))
# sum = 0
# i = 0
# while(i<=num):
#     sum+=i
#     i+=1
# print(sum)

# # problem 5
# num = int(input("enter the number : "))
# fact = 1
# for i in range(1,num +1):
#     fact*=i
# print(fact)
        
# # problem 6
# rows = int(input("enter the no.of rows : "))
# for i in range(1,rows+1):
#     print(" "* (rows - i),end="")
#     print("*" *(2*i-1),end="")
#     print("")
    
# # problem 7
# rows = int(input("enter the no.of rows : "))
# for i in range(1,rows+1):
#     print("*"*(i),end="")
#     print("")

# problem 8
rows = int(input("enter the no.of rows : "))
for i in range(1,rows+1):
    if(i==1 or i==rows):
        print("*"*rows,end="")
    else:
        print("*",end="")
        print(" "*(rows-2),end="")
        print("*",end="")
    print(" ")
        
        
