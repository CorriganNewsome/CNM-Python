# NewsomeP5
# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: Use functions to calcuolate disance between two points.

import math


## A “header” function that takes no parameters and returns nothing that displays a header. The header will print a summary explaining the purpose of the program.
def header():
    print("This program is used to calculate the distance between two points")


## A “get_location” function that takes no parameters, asks the user for a latitude and longitude and returns a tuple or list with the latitude and longitude. Make sure you tell the user what units to enter their information in!
def get_location():
    location = [0, 0]
    location[0] = float(input("Please enter a latitude: "))
    location[1] = float(input("Please enter a longitude: "))
    location = tuple(location)
    return location


# A “distance” function that takes two tuples, each with a latitude and longitude, calculates the distance between those two geographic points and returns the distance.
def distance(location1, location2):
    latitude1 = math.radians(location1[0])
    longitude1 = math.radians(location1[1])
    latitude2 = math.radians(location2[0])
    longitude2 = math.radians(location2[1])
    # Calculate haversine formula
    R = 6371
    A = math.pow(math.sin((latitude1 - latitude2) / 2), 2) + math.cos(
        latitude1
    ) * math.cos(latitude2) * math.pow((math.sin(longitude1 - longitude2) / 2), 2)
    print("A:", A)
    C = 2 * math.atan2(math.sqrt(A), math.sqrt(1 - A))
    return R * C


def displayResults(location1, location2, distance):
    print(f"The distance from {location1} to {location2} is {distance} kilometers")


def main():
    # Call the Header function that displays a header.
    header()

    # Call the get_location function to get the first location.
    location1 = get_location()
    print("Location 1:", location1)

    # Call the get_location function again to get the second location.
    location2 = get_location()
    print("Location 2:", location2)

    # Call the distance function passing in the two locations above as arguments.
    dist = distance(location1, location2)

    # Display a nicely formatted message to the user telling them the distance between those two locations.
    displayResults(location1, location2, dist)


# Finally ask the user if they want to do another.
def doAnother():
    response = input("Do you want to calculate more points? (y/n)")
    another = response.strip()[0].lower() == "y"
    return another


if __name__ == "__main__":
    main()

while doAnother() == True:
    main()
else:
    print("Thank you")
