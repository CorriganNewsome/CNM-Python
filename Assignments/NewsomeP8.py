# NewsomeP7
# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: To demonstrate error handling.

import math


class GeoPoint:
    def __init__(self):
        self.lat = 0.0
        self.lon = 0.0
        self.description = ""

    def setPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def getPoint(self):
        return [self.lat, self.lon]

    def distance(self, lat, lon):
        # Calculate distance using Haversine formula
        R = 6371  # Radius of the Earth in kilometers

        lat1 = math.radians(self.lat)
        lon1 = math.radians(self.lon)
        lat2 = math.radians(lat)
        lon2 = math.radians(lon)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1) * math.cos(
            lat2
        ) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description


# Instiantiate two points
point1 = GeoPoint()
point2 = GeoPoint()

# Set point1's location and description
point1.setPoint(40.7128, 74.0060)
point1.setDescription("New York, NY")

# Set point2's location and description
point2.setPoint(34.0549, 118.2426)
point2.setDescription("Las Angeles, CA")


while True:
    try:  # Adding error handling.
        user_input = input("Enter your location (latitude, longitude): ")
        lat, lon = map(float, user_input.split(","))

        distance_to_one = point1.distance(lat, lon)
        distance_to_two = point2.distance(lat, lon)

        if distance_to_one < distance_to_two:
            closest_point = point1
        else:
            closest_point = point2

        print(
            f"You are closest to: {closest_point.getDescription()} \n Which is located at {closest_point.getPoint()}"
        )
    except ValueError:  # What will print if error occurs.
        print("Error, you must enter two numeric values only")

    except Exception as exc:
        print(f"Error! {exc}")

    do_another = input("Do another (y/n)? ")
    if do_another.lower() != "y":
        print("Thank you for using my lat and long program")
        break
