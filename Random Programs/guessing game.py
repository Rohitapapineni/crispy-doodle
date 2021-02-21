import random
chance=1
num=random.randint(1,20)
while chance<6:
    guess=int(input("enter"))
    if guess==num:
        print("you win")
        break
    chance=chance+1
else:
    print("you lose")
#wrong syntax, needs to be corrected
    

