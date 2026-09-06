# temperature converter
# def celsius_to_fahrenheit(celsius):
# celsius = 5/9 * (fahrenheit - 32)
# return fahrenheit 
# def fahrenheit_to_celsius(fahrenheit):
# fahrenheit = (celsius * 9/5) + 32
# return celsius
# def fahrenheit_to_kelvin(fahrenheit):
# kelvin = (fahrenheit - 32) * 5/9 + 273.15
#return kelvin
#def kelvin_to_fahrenheit(kelvin):
# fahrenheit = (kelvin - 273.15) * 9/5 + 32
#return fahrenheit
# def celsius_to_kelvin(celsius):
# kelvin = celsius + 273.15
# return kelvin
#def kelvin_to_celsius(kelvin):
# celsius = kelvin - 273.15
# return celsius


# temp = float(input("Enter the temperature: "))
# then 
# check the conditio in which kelvin < 0:

# while temp < 0:
# print("Temperature in Kelvin cannot be less than 0.")
# return False
# 
#choice makes sense
# first we have to ask the choices from at the printed the cases of temperature.
#  if choice == "1":
#  print("choice 1")
# continue
# simultaneous for all cases
# try and catach error


# Temperature Converter


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    return kelvin


# Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return fahrenheit


# Celsius to Kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


# Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


# Main program
while True:

    print("\n===== Temperature Converter =====")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Fahrenheit → Kelvin")
    print("4. Kelvin → Fahrenheit")
    print("5. Celsius → Kelvin")
    print("6. Kelvin → Celsius")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Exit
    if choice == "7":
        print("Thank you for using Temperature Converter!")
        break

    # Check valid choice
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please select 1-7.")
        continue

    # Take temperature input
    while True:

        try:
            temperature = float(input("Enter temperature: "))

            # Physical validation
            if choice in ["4", "6"] and temperature < 0:
                print("Invalid temperature. Kelvin cannot be below 0.")
                continue

            if choice in ["1", "5"] and temperature < -273.15:
                print("Invalid temperature. Celsius cannot be below -273.15°C.")
                continue

            if choice in ["3"] and temperature < -459.67:
                print("Invalid temperature. Fahrenheit cannot be below -459.67°F.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Perform conversion
    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature:.2f} °C = {result:.2f} °F")

    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature:.2f} °F = {result:.2f} °C")

    elif choice == "3":
        result = fahrenheit_to_kelvin(temperature)
        print(f"{temperature:.2f} °F = {result:.2f} K")

    elif choice == "4":
        result = kelvin_to_fahrenheit(temperature)
        print(f"{temperature:.2f} K = {result:.2f} °F")

    elif choice == "5":
        result = celsius_to_kelvin(temperature)
        print(f"{temperature:.2f} °C = {result:.2f} K")

    elif choice == "6":
        result = kelvin_to_celsius(temperature)
        print(f"{temperature:.2f} K = {result:.2f} °C")