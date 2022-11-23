#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 21, 2022
# This program asks the user for the temperature
# in celsius and then it converts it to fahrenheit
# The program will then display the converted temperature to the user


# This function converts celsius to fahrenheit and then displays it
def fahrenheit():
    # Gets celsius from user
    celsius = input("Enter the temperature in degrees celsius (°C): ")

    # Checks for exceptions
    try:
        # Converts celsius variable to float
        celsius = float(celsius)

    # In the event of an exception
    except:
        print("You must enter a number for celsius!")

    # Valid user input
    else:
        # Calculates the fahrenheit of the user input
        fahrenheit = (9 / 5) * celsius + 32

        # Displays the celsius to fahrenheit conversion to user
        print(f"{celsius}°C is equal to {fahrenheit}°F")


def main():
    # Displays Program Title
    print("Celsius to Fahrenheit Program")

    # Calls fahrenheit() function
    fahrenheit()


if __name__ == "__main__":
    main()
