## In your program define a class called GeoPoint that will have the following:
# An init (self) method that will set two attributes (variables) called self.lat, self.lon for the location of that point. The init method will also initialize a description attribute (variable) that will start off as the empty string “”.
# A SetPoint(self, lat, lon) method that will set the values of self.lat, self.lon
# A GetPoint(self) method that will return a tuple or list with self.lat, self.lon.
# A Distance(self, lat, lon) method that will figure out the distance between the object’s self.lat, self.lon and lat, lon parameters passed in.
# A SetDescription(self, description) method that will set the objects self.description attribute (variable).
# A GetDescription(self) method that will return the objects self.description attribute.
## In the main part of your program do the following:
# Instantiate two points
# Use the SetPoint and SetDescription methods to set each of the points locations and descriptions. Make sure they have different coordinates and different descriptions.
# Inside a “Do another (y/n)?” loop do the following:
# Ask the user for their location. You can ask for coordinates in three inputs or ask them for their coordinates in one input with each element separated by a coma.
# Use point1 and point2’s Distance method to find the distance from each point to the user’s location
# distanceToOne = point1.Distance(lat, lon)
# distanceToTwo = point2.Distance(lat, lon)
## Tell the user which point they are closest to in this format:
# You are closest to <description> which is located at <point’s coordinates>
# Ask “Do another (y/n)?” and loop if they respond with ‘y’
