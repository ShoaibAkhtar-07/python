import random
computer = (random.randint(1, 3))
name = input("enter your name : ")
print(f"COMPUTER vs {name}")
print("welcome to ~~~~Rock,Paper and Scissor~~~~ game")
print("enter '1' for ROCK , '2' for paper ,'3' for  scissor")

for i in range(1,5):
    
    yournum =int(input("enter your option : "))
    dig_name={
        1 : "ROCK",
        2 : "PAPER",
        3 : "SCISSOR"
    }
    print(f"COMPUTER has choosen : {dig_name[computer]}")
    print(f"you have choosen : {dig_name[yournum]}")

    if(computer == yournum):
        print("match has DRAWN")
    else:
        if(computer==1 and yournum==2):
            print("you WON")
        elif(computer==1 and yournum==3):
            print("you LOST")
        elif(computer==2 and yournum==1):
            print("you LOST")
        elif(computer==2 and yournum==3):
            print("you WON")
        elif(computer==3 and yournum==1):
            print("you WON")
        elif(computer==3 and yournum==2):
            print("you LOST")
        else:
            print("something went wrong")
        
 