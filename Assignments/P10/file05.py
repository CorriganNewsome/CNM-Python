filename = "locations.txt"

with open(filename, 'r') as f:
        # Find columns and rows
        columns = int(f.readline())
        rows = int(f.readline())
        your_list = [[f.readline().strip() for i in range(rows)] for j in range(columns)]

print(your_list)