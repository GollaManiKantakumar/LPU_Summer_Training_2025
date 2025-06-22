import random as ran
n=ran.randint(1,10)

while( True ):
    try :
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < n:
            print("Too small")
        elif guess > n:
            print("Too big")
        else:
            print("You guess right")
            break
    except ValueError:
        print("Invalid input.Please enter a number between 1 and 10")


