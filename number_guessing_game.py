import random
import math
lower=int(input("enter lower range="))
upper=int(input("enter upper range="))
x=random.randint(lower,upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")
count=0
flag = False
while count<total_chances:
    count=count+1
    guess=int(input("Guess a number="))

    if guess==x:
        print("congratulations you did it in ",count," tries")
        flag = True
        break
    elif guess>x:
        print("you Guesses too large number!")
    else:
        print("you guessed too small number!")  

if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
   