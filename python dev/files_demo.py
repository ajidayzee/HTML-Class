#The codes on lines 2 ans 3 perform the same functions
#courses_file = open("courses.txt")
with open("courses.txt") as courses_file:
    for line in courses_file:
        parts = line.split(",")
        name = parts[0]
        grade = float(parts[1])
        bonus_grade = grade + 3
        print(f"{name} --- Grade:{grade} --- After Bonus:{bonus_grade}")
        print(f"")
        print()
    print("Goodbye!")
print("The file is closed now.")        