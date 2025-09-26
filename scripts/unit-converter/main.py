from unit_converter.utils import (
    miles_to_km,
    inches_to_centimeter,
    fahrenheit_to_celsius,
)

# main.py

user_choice = input(
    "Please choose a conversion category:\n1. Temperature (Fahrenheit to Celsius)\n2. Length (Miles to Kilometers)\n3. Length (Inches to Centimeters)\nEnter your choice (1, 2, or 3): "
)


# converting fahrenheit to celsius
if user_choice == "1":
    while True:
        try:
            fahrenheit_input = float(
                input(
                    "Please enter the temperature in Fahrenheit you would like to convert to Celsius:\n"
                )
            )

            result = fahrenheit_to_celsius(fahrenheit_input)
            print(f"{fahrenheit_input}°F is equal to {result:.2f}°C")
            break

        except ValueError:
            print("Invalid input. Please enter a number.")


# converting miles to kilometers
elif user_choice == "2":
    while True:
        try:
            miles_input = float(
                input(
                    "Please enter the distance in miles you would like to convert to kilometers:\n"
                )
            )

            result = miles_to_km(miles_input)
            print(f"{miles_input} miles is equal to {result:.2f} kilometers")
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

# converting inches to centimeter
elif user_choice == "3":
    while True:
        try:
            inches_input = float(
                input(
                    "Please enter the length in inches you would like to convert to centimeters:\n"
                )
            )

            result = inches_to_centimeter(inches_input)
            print(f"{inches_input} inches is equal to {result:.2f} centimeters")
            break

        except ValueError:
            print("Invalid input. Please enter a number.")
