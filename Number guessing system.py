import random

target=random.randint(1,100)
while True:
    userChoice=(input("guess the number or Quit(Q):"))
    if(userChoice=="Q"):
        print("---GAME OVER---")
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("success:correct guess!!")
        print("congratulations  you are won...")
        break
    if(userChoice<target):
        print("your number was too small,take a bigger guess..")
    else:
        print("your number was too big.Take a smaller guess..")
    print("----GAME OVER-----")
