sentence = "With a moo-moo here, and a moo-moo there"

# .find retuns -1 if substring not found
locationOfMoo = sentence.find("blah")
print("With .find")
print(locationOfMoo)
print(sentence[locationOfMoo:])

# .index causes error if substring not found
indexOfMoo = sentence.index("blah")
print("\n With .index")
print(indexOfMoo)
print(sentence[indexOfMoo])
