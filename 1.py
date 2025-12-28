# 1. write a random number generates random numbers between 1 to 6 (simulates a dice).
import random
while True:
    print("="*55)
    print("**Rolling the dice**")
    print("="*55)
    num = random.randint(1,6)
    if num == 6:
        print("Hey.....you got",6,".....congratulation!!")
    elif num == 1:
        print("well tried.......but you got",num)
    else:
        print("you got : ",num)
    ch = input("Roll again ? (Y/N) : ")
    if ch in 'Nn':
        break
print("!!! THANKS FOR PLAYING !!!")