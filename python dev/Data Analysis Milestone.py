import csv

# Load the dataset
with open('life-expectancy.csv') as csv_file:
    reader = csv.reader(csv_file)

    # Initialize the lowest and highest life expectancy values
    lowest_life_expectancy = None
    highest_life_expectancy = None

    # Iterate through the data line by line
    for row in reader:
        # Split each line into parts
        country = row[0]
        year = (row[1])
        life_expectancy = (row[2])

        # Update the lowest and highest life expectancy values as needed
        if lowest_life_expectancy is None or life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            lowest_life_expectancy_country = country
            lowest_life_expectancy_year = year
        elif highest_life_expectancy is None or life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            highest_life_expectancy_country = country
            highest_life_expectancy_year = year

# Display the lowest and highest life expectancy values
print('The lowest life expectancy in the dataset is {} for {} in {}'.format(lowest_life_expectancy, lowest_life_expectancy_country, lowest_life_expectancy_year))
print('The highest life expectancy in the dataset is {} for {} in {}'.format(highest_life_expectancy, highest_life_expectancy_country, highest_life_expectancy_year))
