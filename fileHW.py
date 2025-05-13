# # problem 1

# f = open("poem.txt","r")
# if("twinkle" in f.read().lower()):
#     print("the word is present")
# else:
#     print("the word is not present")
# f.close()
 
 
# # PROBLEM 2

# import random
# def game():
#     print("U R PLAYING THE GAME")
#     score = random.randint(1,50)
#     with open("hiscore.txt","r") as f:
#         hiscore = f.read()
#         if (hiscore!= ""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
            
#     print(f"your score is {score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
    
            
# game()


# # PROBLEM 3

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i}\n"
#     with open(f"tables.txt/table_{n}","w") as f:
#         f.write(table)
        

# for i in range(2,21):
#     generateTable(i)


# # PROBLEM 4

# with open("donkey.txt","r") as f:
#     content = f.read()
# newcontent = content.lower().replace("donkeys","######")
# with open("donkey.txt","w") as f:
#     f.write(newcontent)

# # PROBLEM 5

# words = ["donkeys","prideful","shallow","vain","flawed"]
# with open("donkey.txt","r") as f:
#     content = f.read()
# for word in words:
#     content=content.lower().replace(word,"#"*len(word))
# with open("donkey.txt","w") as f:
#     f.write(content)
    
# PROBLEM 6 and 7

with open("log.txt", "r") as f:
    line = f.readline().lower()
    
    if "python" in line:
        print(f"The word is PRESENT in the file: {line}.")
    else:
        print("The word is NOT PRESENT in the file.")
        
    
