# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: To help user calculate the surface area and volume of a square
# pyramid

# Import Math Library
import math

# Recieve inputs from user
baseLength = float(
    input('Please enter the are of the base(in feet): '))
    height = float(
    input('Please enter slant height of pyramid(in feet): '))

# Create formulas
slantHeight = math.sqrt((height**2) + (baseLength/2)**2)

surfaceArea = 1/2 * (math.sqrt(baseLength**2) + 4 * (height))

volume = ((baseLength**2) * height)/3

# Print results
print('The surface area is', surfaceArea)
print('The volume is', volume)