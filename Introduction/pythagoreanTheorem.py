# Display a header explain the program
print('Solving Pythagorean Theorem')

# Get length of one side from user
givenSide = float(input('Please enter the length of given side: '))
# Get length of the hypotenus
hypotenus = float(input('Please enter hypotenus in inches: '))
# Calculate the length of the side
calculatedSide = (hypotenus**2 - givenSide**2)**0.5

# Display Result
print('\nThe length of the calculated side is,', calculatedSide)

# Thank you message
print('\nThank you for using the Pythagorean Theorem calculator')