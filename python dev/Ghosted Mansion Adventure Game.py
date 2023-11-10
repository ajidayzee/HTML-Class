#To exceed requirement I showed my program to two people, they played it, I showed my code and explained how it worked.
#They really enjoyed the game and they were excited at how inputing prompts could make a simple and enjoyable game.
#It was a nice experience and it encourages me to put in more efforts into programming.
#Ghosted Mansion Adventure Game
#Welcome Message
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
    living_room_choice = input("")
    print()
    if living_room_choice.lower() == "keep":
        print("You are keeping the dog.")
        print("Would you take care of the dog? YES or NO")
        print()
        #KEEP choice
        keep_choice = input("")
        print()
        if keep_choice.lower() == "yes":
            print("That is very good of you.")
            print("GAME OVER!")
        elif keep_choice.lower() == "no":
            print("That is very bad of you.")
            print("GAME OVER!")
        else:
            print("Oops, wrong choice. Pick from the capitalized words.")
            print("Play again.")
    elif living_room_choice.lower() == "kick":
        print("You kicked the dog. The dog is bleeding.")
        print("Would you take the dog to the hospital? YES or NO")
        print()
        #KICK choice
        kick_choice = input("")
        print()
        if kick_choice.lower() == "yes":
            print("The dog would be cared-for.")
            print("GAME OVER!")
        elif kick_choice.lower() == "no":
            print("The dog would die.")
            print("GAME OVER!")
    else:
        print("Oops, wrong choice. Pick from the capitalized words.")
        print("Play again.")
    print()       
elif room_choice.lower() == "dining room":
    print("You are now in the dining room.")
    print("There is an injured cat in the dining room.")
    print("Do you want to HELP or PASS or HIT?")
    print()
    dining_room_choice = input("")
    print()
    if dining_room_choice.lower() == "help":
        print("You are helping the cat")
        print("Did you give the cat first aid? YES or NO")
        print()
        #HELP choice
        help_choice = input("")
        print()
        if help_choice.lower() == "yes":
            print("The first aid sustained the cat before you took it to the hospital")
            print("GAME OVER!")
        elif help_choice.lower() == "no":
            print("You did not give the cat first aid, the injury worsened and it made the cat paralyzed")
            print("GAME OVER!")
        else:
            print("Oops, wrong choice. Pick from the capitalized words.")
            print("Play again.")
    elif dining_room_choice.lower() == "pass":
        print("You passed by the cat. And it suffered and died in pain.")
        print("Do you want to BURY or LEAVE the cat?")
        print()
        #PAIN choice
        pain_choice = input("")
        print()
        if pain_choice.lower() == "bury":
            print("You gave the cat a befitting burial.")
            print("GAME OVER!")
        elif pain_choice.lower() == "leave":
            print("The cat decays and smells all over the mansion.")
            print("GAME OVER!")
        else:
            print("Oops, wrong choice. Pick from the capitalized words.")
            print("Play again.")
    elif dining_room_choice.lower() == "hit":
        print("You hit the cat with a rod. The cat limps and runs away.")
        print("Do you want to RUN after the cat or WATCH the cat run away?")
        print()
        #HIT choice
        hit_choice = input("")
        print()
        if hit_choice.lower() == "run":
            print("You run after the cat and bumped your head.")
            print("GAME OVER!")
        elif hit_choice.lower() == "watch":
            print("You watch the cat run away, and the cat jumped through the window.") 
            print("GAME OVER!")   
    else:
        print("Oops, wrong choice. Pick from the capitalized words.")
        print("Play again.")
else:
    print("Oops, wrong choice. Pick from the capitalized words.")
    print("Play again.")