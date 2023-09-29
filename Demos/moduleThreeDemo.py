## Stiring Formatting Demo

# Ask for user name
name = input("Please enter your name: ")
# Ask for height of wall
height = float(input("Please enter height of wall in ft: "))
# Ask for width of wall
width = float(input("Please enter width of wall in ft: "))
# Ask for sq ft per gallon
sqft = float(input("Please enter sqft of gallon coverage of paint: "))
# Ask for number of coats of paint
numCoats = int(input("Please enter number of coats of paint: "))

# Calculate how many gallons are needed
area = height * width  # sqft
gallonsForOneCoat = area / sqft  # gallons
gallons = gallonsForOneCoat * numCoats  # gallons

# Display results with %s
print(
    f"{name}, the number of gallons needed for a wall that is {height} ft high and {width} ft wide with {numCoats} coats is {gallons} gallons. Thank you {name}"
)
