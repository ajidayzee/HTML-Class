#Windchill
def main():
    try:
        temperature_input = input("Enter temperature (in Celsius or Fahrenheit): ")
        temperature = float(temperature_input)
        if temperature_input.lower().endswith("c"):
            temperature = celsius_to_fahrenheit(temperature)
        
        for wind_speed in range(5, 65, 5):
            wind_chill = calculate_wind_chill(temperature, wind_speed)
            print(f"At {wind_speed} mph, the wind chill is: {wind_chill} °F")
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_wind_chill(temperature, wind_speed):
    fahrenheit_temp = temperature if temperature > -50 else celsius_to_fahrenheit(temperature)
    if wind_speed < 5 or fahrenheit_temp > 50:
        return "N/A"
    wind_chill = 35.74 + 0.6215 * fahrenheit_temp - 35.75 * (wind_speed * 0.16) + 0.4275 * fahrenheit_temp * (wind_speed * 0.16)
    return round(wind_chill, 2)
if __name__ == "__main__":
    main()