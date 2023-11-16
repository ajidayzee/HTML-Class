def get_initial (name, force_uppercase):
    if force_uppercase:
        initial = name[0:1] .upper()
    else:
        initial = name[0:1]    
    return initial

#Ask for someone's name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)
#first_name_initial = get_initial(name = first_name,force_uppercase = False)
#The code above does the same thing as the one above it.
#It assigns values to parameters by name when you call the function.  

middle_name = input('Enter your middle name: ')
middle_name_initial = get_initial(middle_name, False)
#middle_name_initial = get_initial(name = middle_name, force_uppercase = False) 
#The code above does the same thing as the one above it.
#It assigns values to parameters by name when you call the function.

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name, False)
#last_name_initial = get_initial(name = last_name, force_uppercase = True)
#The code above does the same thing as the one above it.
#It assigns values to parameters by name when you call the function. 

print("Your initials are:" + first_name_initial + " " + middle_name_initial + " " + last_name_initial)