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
max_age = 0
max_name = ""

for person in people:
    person = person.strip()
    parts = person.split()
    name = parts[0]
    age = int(parts[1])
    print(person)
    if age > max_age:
        max_age = age
        max_name = name
        print(f"The oldest person is: {max_name} with an age of {max_age}")