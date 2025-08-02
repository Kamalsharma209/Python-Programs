import random

target = random.randint(1 , 100)
while True:
     userChoice = int(input("Guess the Number : "))
     if(userChoice == target):
         print("You Won...!!")
         break
     elif(userChoice<target):
         print("Number is too small... make a big guess...")
     else:
         print("Number is too big.... make a small guess")
print("------------GAME OVER----------------")