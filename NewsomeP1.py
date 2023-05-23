# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: To help user calculate the surface area and volume of a square pyramid

# Recieve inputs from user
peremiterOfBase = float(input('Please enter the perimeter of the base: '))
slantHeight = float(input('Please enter slant height of pyramid: '))
areaOfBase = float(input("Please enter the are of the base: "))

# Create SA formula
surfaceAreaofPyramid = (peremiterOfBase * slantHeight)/2 + areaOfBase
# Print Results
print(surfaceAreaofPyramid)

# Volume of a pyramid V = 1/3(ba)(h)
volume = 1/3 * areaOfBase * slantHeight
print(volume)
