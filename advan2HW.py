from functools import reduce
# # PROBLEM 1

# name=input("enter your name : ")
# marks =int(input("entr your marks : "))
# mbnum=int(input("entr your mobile mumber : "))

# s="The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,mbnum)
# print(s)



# # PROBLEM 2
# n = int(input("Enter the number : "))
# table =[str(n*i) for i in range(1,11)]
# print("\n".join(table))



# # PROBLEM 3

# def divsible5(n):
#     if(n%5)==0:
#         return True
#     return False

# s = [12,24,75,90,15,75,70,600,45,333]
# print(list(filter(divsible5,s)))



# PROBLEM 4
def greater(a,b):
    if(a>b):
        return a
    return b
s = [12,24,75,90,15,75,70,600,45,333]
print(reduce(greater,s))
