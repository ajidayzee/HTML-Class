    #Check First Letter
    if secret_word[0] == guess[0]:
        print(f"{bg_green}{guess[0].capitalize()}{reset}")
    elif guess[0] in secret_word:
        print(f"{bg_yellow}{guess[0].lower()}{reset}")
    else:
        print("_")
    #Check Second Letter 
    if secret_word[1] == guess[1]:
        print(f"{bg_green}{guess[1].capitalize()}{reset}")
    elif guess[1] in secret_word:
        print(f"{bg_yellow}{guess[1].lower()}{reset}")
    else:
        print("_")
    #Check Third letter
    if secret_word[2] == guess[2]:
        print(f"{bg_green}{guess[2].capitalize()}{reset}")
    elif guess[2] in secret_word:
        print(f"{bg_yellow}{guess[2].lower()}{reset}")
    else:
        print("_")  
    #Check Fourth Letter
    if secret_word[3] == guess[3]:
        print(f"{bg_green}{guess[3].capitalize()}{reset}")
    elif guess[3] in secret_word:
        print(f"{bg_yellow}{guess[3].lower()}{reset}")
    else:
        print("_")
    #Check Fifth Letter
    if secret_word[4] == guess[4]:
        print(f"{bg_green}{guess[4].capitalize()}{reset}")
    elif guess[4] in secret_word:
        print(f"{bg_yellow}{guess[4].lower()}{reset}")
    else:
        print("_")