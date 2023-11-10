import pandas as pd

# Load the dataset
df = pd.read_csv('life-expectancy.csv')

# Get the year and country with the lowest life expectancy
lowest_life_expectancy = df.loc[df['Life expectancy'].idxmin()]
lowest_life_expectancy_year = lowest_life_expectancy['Year']
lowest_life_expectancy_country = lowest_life_expectancy['Country']

# Print the results
print('The year and country with the lowest life expectancy in the dataset are {} and {}, respectively.'.format(lowest_life_expectancy_year, lowest_life_expectancy_country))

# Get the year and country with the highest life expectancy
highest_life_expectancy = df.loc[df['Life expectancy'].idxmax()]
highest_life_expectancy_year = highest_life_expectancy['Year']
highest_life_expectancy_country = highest_life_expectancy['Country']

# Print the results
print('The year and country with the highest life expectancy in the dataset are {} and {}, respectively.'.format(highest_life_expectancy_year, highest_life_expectancy_country))
# Get the year from the user
year = int(input('Enter a year: '))

# Filter the dataset for the specified year
df_filtered = df[df['Year'] == year]

# Calculate the average life expectancy for the specified year
average_life_expectancy = df_filtered['Life expectancy'].mean()

# Get the country with the minimum and the one with the maximum life expectancies for the specified year
min_life_expectancy_country = df_filtered['Country'].idxmin()
max_life_expectancy_country = df_filtered['Country'].idxmax()

# Print the results
print('The average life expectancy for the year {} is {}'.format(year, average_life_expectancy))
print('The country with the lowest life expectancy for the year {} is {}'.format(year, min_life_expectancy_country))
print('The country with the highest life expectancy for the year {} is {}'.format(year, max_life_expectancy_country))
