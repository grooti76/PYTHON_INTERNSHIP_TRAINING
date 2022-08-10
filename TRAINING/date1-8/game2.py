import numbers
import random
number = random.randint(1, 10)
guess = int(input("Enter the Number"))
while(True):
    if(guess > number):
        print("Guess another number. The number is too big")
        count = 1
    elif(guess < number):
        print("Guess another number. This is too short")
    else:
        print("You Win")
    break
