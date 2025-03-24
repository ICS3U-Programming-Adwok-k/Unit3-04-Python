#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 24th, 2025
# This program asks the user to enter an integer


def main():
    # Get the user_input(number)
    user_number = int(input("Enter an integer : "))

    # If the number is greater than 0, then it's positive
    if user_number > 0:
        print("The number is a positive number.")

    # If the number is less than 0, then it's negative
    elif user_number < 0:
        print("The number is a negative number.")

    # If the number is 0, then it's just zer
    else:
        print("The number is just zero!")


if __name__ == "__main__":
    main()
