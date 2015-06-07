import random

secret = int(random.uniform(0,10))
print("Guess a number between 0 and 10")
guess = 11

while guess != secret:
    try:
        guess = int(input())
    except ValueError:
        print("Please enter an integer value...")
    except NameError:
	print("Please enter an integer value...")
print("You win!")
