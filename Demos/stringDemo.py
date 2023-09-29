website = "http://www.python.org"
new_website = website[:-3] + "com"
print(new_website)

# String Length Demo
title = input("Please enter text to center: ")
num_letters = len(title)
print(title, "has", num_letters, "letters in it")
# width = 80
halfway = width // 2
start_at = halfway - num_letters // 2
line = start_at * " " + title
print(line)
