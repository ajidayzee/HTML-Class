#Word Puzzle Game Milestone
secret_word = "zarahemla"
guess_counter = 1
print()
print("Welcome to the word guessing game!")
print()
guess = input("What is your guess? ")
print()
while guess.lower() != secret_word:
    print("Oops, you guessed wrong. Try again.")
    guess = input("What is your guess? ")
    guess_counter = guess_counter + 1
print("Congratulations!. You guessed right.")
print("You had", guess_counter , "guesses.")  