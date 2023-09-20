# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: To help user calculate the surface area and volume of a square pyramid.

# Import Math Library
import math

# Recieve inputs from user
baseLength = float(
    input('Please enter the length of the base(in feet): '))
height = float(
    input('Please enter height of pyramid(in feet): '))

# Create formulas

surfaceArea = baseLength * (math.sqrt(baseLength**2 + 4 * (height**2)))

volume = ((baseLength**2) * height)/3

# Print results
print('The surface area is', surfaceArea)
print('The volume is', volume)