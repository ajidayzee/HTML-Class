# Function to read the dataset from a CSV file
def read_csv ():
    data = []
    with open("life-expextancy", 'r') as file:
        header = next(file)  # Read the header and ignore it
        for line in file:
            year, country, life_expectancy = line.strip().split(',')
            data.append((int(year), country, float(life_expectancy)))
    return data

# Function to find the year and country with the lowest life expectancy
def find_lowest_life_expectancy(data):
    min_life_expectancy = min(data, key=lambda x: x[2])
    return min_life_expectancy

# Function to find the year and country with the highest life expectancy
def find_highest_life_expectancy(data):
    max_life_expectancy = max(data, key=lambda x: x[2])
    return max_life_expectancy

# Function to calculate the average life expectancy for a given year
def calculate_average_life_expectancy(data, year):
    year_data = [item for item in data if item[0] == year]
    if not year_data:
        return None
    average = sum(item[2] for item in year_data) / len(year_data)
    return average

# Function to find the country with the minimum and maximum life expectancies for a given year
def find_min_max_countries(data, year):
    year_data = [item for item in data if item[0] == year]
    if not year_data:
        return None, None
    min_country = min(year_data, key=lambda x: x[2])[1]
    max_country = max(year_data, key=lambda x: x[2])[1]
    return min_country, max_country

# Main function
#if _name_ == '_main_':
    file_path = 'your_dataset.csv'  # Replace with the actual file path
    dataset = read_csv(file_path)

    lowest_year, lowest_country, lowest_life_expectancy = find_lowest_life_expectancy(dataset)
    highest_year, highest_country, highest_life_expectancy = find_highest_life_expectancy(dataset)

    print(f"The year and country with the lowest life expectancy: Year {lowest_year}, Country {lowest_country}, Life Expectancy {lowest_life_expectancy}")
    print(f"The year and country with the highest life expectancy: Year {highest_year}, Country {highest_country}, Life Expectancy {highest_life_expectancy}")

    year_input = int(input("Enter a year: "))
    average_life_expectancy = calculate_average_life_expectancy(dataset, year_input)

    if average_life_expectancy is not None:
        min_country, max_country = find_min_max_countries(dataset, year_input)
        print(f"Average life expectancy for {year_input}: {average_life_expectancy}")
        print(f"Country with the minimum life expectancy for {year_input}: {min_country}")
        print(f"Country with the maximum life expectancy for {year_input}: {max_country}")
    else:
        print(f"No data available for the year {year_input}")