# NewsomeP7
# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: To create a GUI.

import math
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame
win = Tk()

# Set the geometry of Tkinter frame
win.geometry("750x250")


def display_text():
    global entry
    string = entry.get()
    label.configure(text=string)


# Initialize a Label to display the User Input
label = Label(win, text="", font=("Courier 22 bold"))
label.pack()

# Create a Button to validate Entry Widget
ttk.Button(win, text="Okay", width=20, command=display_text).pack(pady=20)


class GeoPoint:
    def __init__(self, lat=0, lon=0, description="TBD"):
        self.lat = lat
        self.lon = lon
        self.description = description

    def setPoint(self, point):
        self.lat = point[0]
        self.lon = point[1]

    def getPoint(self):
        return self.lat, self.lon

    def distance(self, point):
        # Calculate distance using Haversine formula
        R = 6371  # Radius of the Earth in kilometers

        lat1 = math.radians(self.point[0])
        lon1 = math.radians(self.point[1])
        lat2 = math.radians(self.point[0])
        lon2 = math.radians(self.point[1])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1) * math.cos(
            lat2
        ) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance

    def setDescription(self, descriptionString):
        self.description = descriptionString

    def getDescription(self):
        return self.description

    point = property(getPoint, setPoint)
    descriptionString = property(getDescription, setDescription)


# Instiantiate two points
point1 = GeoPoint()
point2 = GeoPoint()

# Set point1's location and description
point1.point = (40.7128, 74.0060)
point1.description = "New York, NY"

# Set point2's location and description
point2.point = (34.0549, 118.2426)
point2.description = "Las Angeles, CA"

# Create an Entry widget to accept User Input
entry = Entry(win, width=40)
entry.focus_set()
entry.pack()

while True:
    try:  # Adding error handling.
        user_input = input("Enter your location (latitude, longitude): ")
        userPoint = map(float, user_input.split(","))

        distance_to_one = point1.distance(userPoint)
        distance_to_two = point2.distance(userPoint)

        if distance_to_one < distance_to_two:
            closest_point = point1
        else:
            closest_point = point2

        print(
            f"You are closest to: {closest_point.getDescription()} \n Which is located at {closest_point.getPoint()}"
        )
    except ValueError:  # What will print if error occurs.
        print("Error, you must enter two numeric values only")

    except Exception as exc:  # Catch any errors we may have missed.
        print(f"Error! {exc}")

    do_another = input("Do another (y/n)? ")
    if do_another.lower() != "y":
        print("Thank you for using my lat and long program")
        break

win.mainloop()
