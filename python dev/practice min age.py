people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10",
]
min_age = 1000
min_name = ""

for person in people:
    person = person.strip()
    parts = person.split()
    name = parts[0]
    age = int(parts[1])
    print(person)
    #print(name,end=" ")
    #print(age)
    if age < min_age:
        min_age = age
        min_name = name
        print(f"The youngest person is: {min_name} with an age of {min_age}")      
            