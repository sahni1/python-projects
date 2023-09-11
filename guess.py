import random
import math

lower=int(input("Enter Lower bound:-"))

upper=int(input("Enter Upper bound"))

                
x=random.randint(lower,upper)

print("\nyou have only" , round(math.log(upper - lower +1,2)) ,"chances to guess the integer\n")

count=0

while count < math.log(upper - lower +1,2):
    count=count+1

    guess=int(input("Guess a no."))

    if guess > x:
        print("Try Again! You guessed too high")
    
    elif guess < x:
        print("You Guessed Too low!")

    elif guess==x:
        print("congratulations")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
