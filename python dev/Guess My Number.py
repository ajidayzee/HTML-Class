import random
magic_number = random.randint(1, 100)
guess = -1
guess = int(input("What is your guess? "))
while guess != magic_number:
    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it!")

