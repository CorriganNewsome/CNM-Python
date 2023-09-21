months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

endings = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 
           'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'st', 'nd', 
           'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'st']

# Get inputs from users
month = input('Pick a Month (1-12)')
day = input('Pick a Day (1-31): ')
year = input('Please enter Year: ')

# Calculate Month
month_number = int(month)
month_name = months[month_number-1]

# Calculate day and ordinal
day_number = int(day)
ordinal = day+endings[day_number-1]

# Print results
print(month_name + ' ' + ordinal + ' ' + year)
