import csv
with open("life-expectancy.csv", "r") as data:
    csv_reader = csv.reader(data)
    #year_of_interest = input("Enter the year of interest: ")    
    #for line in data:
    for line in csv_reader:
        #line = line.split(',')
        #parts = line.split()
        #entity = line[0]
        #code = line[1]
        #year = line[2]
        #life_expectancy = line[3]
        print(line)