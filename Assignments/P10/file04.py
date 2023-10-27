filename = "locations.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

# printing the data
print(lines)
#filename.close()