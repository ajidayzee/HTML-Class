#Word Puzzle Game 
#The comments below describes what i have done to show creativity.
#When a letter of the hint is capitalised and has a green background, it means the letter is in the word and in the right position.
#When a letter of the hint is in lower-case and has a yellow background, it means the letter is in the word but not in the right position.
#When a letter of the hint shows "_", it means the letter is not in the word.
#The guess is always a 5 letter word
import random
secret_words = random.choice (["ammon", "brass", "arrow", "limhi", "jared"])
guess_counter = 1
#Hint Colors
bg_green = "\u001b[42m"
bg_yellow = "\u001b[43m"
reset = "\u001b[0m"
print()
print("Welcome to the word guessing game!")
print()
print("The guess is a WORD or NAME from the Book Of Mormon.")
print()
guess = input("What is your guess? ")
print()
while guess.lower() != secret_words:
    print("\nOops, you guessed wrong. Try again.")
    guess = input("\nWhat is your guess? ")
    print("\nYour hint is: ")
    guess_counter = guess_counter + 1    
    #Hint Checking Each Letter
    for i in range(0,5):
        while len(guess) != len(secret_words) :
            print("\nSorry, the guess is a 5 letter word.")
            print("\nPlease enter a 5 letter word.")
            guess = input("\nWhat is your guess? ")
            guess_counter = guess_counter + 1
        if secret_words[i] == guess[i]:
            print(f"{bg_green}{guess[i].capitalize()}{reset}" , " ", end="")
        elif guess[i] in secret_words:
            print(f"{bg_yellow}{guess[i].lower()}{reset}", " ", end="")
        else:
            print("_" , " " , end="")
print("\n")                                     
print("\nCongratulations!. You guessed right.")
print("\nYou had", guess_counter , "guesses.")