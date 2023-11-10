#Word Puzzle Game Milestone
secret_word = "zoram"
hint = " "
counter = 1
print()
print("Welcome to the word guessing game!")
print()
guess = input("What is your guess? ")
print()
for i, letter in enumerate (secret_word):
    if i < len(guess) and letter.lower() == (guess)[i]:
        hint += letter.upper()
    elif letter.lower() in guess:
        hint += letter.lower()
    else:
        hint += "_ " 
print(f"Your hint is:{hint}")
while guess.lower() != secret_word:
    print("Oops, you guessed wrong. Try again.")
    print(f"Your hint is:{hint}")
    guess = input("What is your guess? ")
    counter = counter + 1
    if len(guess) != len(secret_word):
        print("Word must be 5 characters long.")
    else:
        for i, letter in enumerate (secret_word):
            if i < len(guess) and letter.lower() == (guess)[i]:
             hint += letter.upper()
            elif letter.lower() in guess:
             hint += letter.lower()
            else:
             hint += "_ " 
            print(f"Your hint is:{hint}")        
print("Congratulations!. You guessed right.")
print("You had", counter , "guesses.")    