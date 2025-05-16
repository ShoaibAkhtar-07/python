# # PROBLEM  1

# try:
#     with open("1.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("3.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
    
# print("Thank you my dear")



# # PROBLEM 2 

# my_list=[1,2,3,4,5,6,7,8,9,10]

# for index,item in enumerate(my_list):
#     if(index == 2) or (index == 4) or (index == 6):
#         print(item)



# PROBLEM 3

n : int = int(input("Enter the number : "))
table : list[int] = [n*i for i in range(1,11)]
print(table) 