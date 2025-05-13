# a =int(input("enter the age : "))
# b =int(input("enter the age : "))
# c =int(input("enter the age : "))
# d =int(input("enter the age : "))
# if(a>b and a>c and a>c):
#    print("a is greater : ",a)
# elif(b>a and b>c and b>c):
#     print("b is greater : ",b)
# elif(c>a and c>c and c>d):
#     print("c is greater : ",c)
# elif(d>a and d>c and d>b):
#     print("d is greater : ",d)
# a1 = "shoaib"
# a2 = "akhtar"
# a3 ="dornakal"
# a4 = "2005"

# text = input("enter the message here :")

# if(a1.lower in text.lower and a2.lower in text.lower and a3.lower in text.lower and a4.lower in text.lower):
#     print("you  have entered  correct details")
# else:
#     print("you entered  have incorrect details ")
l =["shoaib", "akhtar","nazir","zulekha","ayesha","sumaiya"]
name = input("enter your name : ")
if(name.lower() in l.lower()):
    print("your name is in the list ")
else:
    print("your name is not in the list")
