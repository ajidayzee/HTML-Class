#Ghosted Mansion Adventure Game
#Welcome Message
play = input("Would you like to play? YES or NO:"+" ")
if play.lower() == "yes":
#print() is used for proper spacing and alignment
    print("Welcome to the Ghosted Mansion Adventure Game!")
    print()    
    print("You are the only child of a Billionaire who just passed away,leaving this mansion.")
    print("As the new owner of the mansion, you decided to visit the mansion.")
    print("The mansion is screaky. You walk in through the door ")
    print("Do you want to enter the LIVING ROOM or the DINING ROOM")
    print()
#ROOM choice
    room_choice = input("")
    print()
    if room_choice.lower() == "living room":
        print("You are now in the living room.")
        print("There is a dog in the living room.") 
        print("Do you want to KEEP or KICK?")
        print()
    elif room_choice.lower() == "dining room":
        print("You are now in the dining room.")
        print("There is an injured cat in the dining room.")
        print("Do you want to HELP or PASS or HIT?")
        print()
    else:
        print("Oops, wrong choice. Pick from the capitalized words.")
        print("Play again.")
elif play.lower() == "no" :
    print("This game is really cool.")
    play = input("Do you still want to play? YES or NO:"+" ")
else:
    print("Oops, wrong choice. Pick from the capitalized words.")
    print("Play again.")           