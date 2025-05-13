# # problem 1
# def greater(a,b,c):
#     if(a>b and a>c):
#         print("a is greater")
#     elif(b>a and b>c):
#         print("b is greater")
#     else:
#         print("c is greater")
#     return "done"
     
        
# a =int(input("enter a value : "))
# b =int(input("enter b value : "))
# c =int(input("enter c value : "))
# print(f"{greater(a,b,c)}")

# #  problem 2
# def celtofar(celsius):
#     return (celsius*(9.0/5.0))+32

# celsius = float(input("enter celsius value : "))
# print(f"{celtofar(celsius)}")


# # problem 3
# def sumofn(n):
#     if(n==1):
#         return 1
#     return n+sumofn(n-1)
# n=int(input("enter the number : "))
# print(f"the sum of {n} is {sumofn(n)}")

# # [problem 4]
# def star_pattern(rows):
#     for i in range(1,rows+1):
#         print("*"*(rows-i+1))

# rows = int(input("enter the no.of rows : "))
# star_pattern(rows)

# # problem 5
# def inch_to_cms(inch):
#     print(inch * 2.54)
    
# inches =int(input("enter the value : "))
# inch_to_cms(inches)

# # problem 6
# def mul(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# n = int(input("enter the number : "))
# mul(n)

# # problem 7
# def remove(l,word):
#     for item in l:
#         l.remove(word)
#         print(l)
#         return l
# l = ["apple","ball","cat","dog","call","mall","all"]
# print(l)
# word=input("enter the word : ")
# remove(l,word)

 # problem 8
def remove(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
            return n
l = ["apple","ball","cat","dog","call","mall","all"]
word=input("enter the word : ")
print(remove(l,word))
 


