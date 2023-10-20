# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: To convert tempatures from C to F and vice versa.

import math


def celciusToFahrenheit(C):
    F = C * (9 / 5) + 32
    return F


def FahrenheitToCelcius(F):
    C = (F - 32) * 5 / 9
    return C


def goodbye():
    print("Thank you for using the tempature converter program")


while True:
    print("Welcome to the tempature converter.")
    userInput = input("Would you like to convert Celcius to Farenheight? y/n: ")

    if userInput == "y":
        inputCelcius = float(input("Please enter your tempature, in Celcius: "))
        print(
            f"Your temapture is {inputCelcius}, your tempature in Farenheight is {celciusToFahrenheit(inputCelcius)}"
        )

    elif userInput == "n":
        userInput = input("Would you like to convert Farenheight to Celcius? y/n: ")
        if userInput.lower() == "y":
            inputFarenheight = float(
                input("Please enter your tempature, in Farenheight: ")
            )
            print(
                f"Your temapture is {inputFarenheight}, your tempature in Farenheight is {FahrenheitToCelcius(inputFarenheight)}"
            )
        elif userInput != "y":
            goodbye()
            break
    else:
        break

    do_another = input("Do another (y/n)? ")
    if do_another.lower() != "y":
        goodbye()
        break
