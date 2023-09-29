sentence = "With a moo-moo here, and a moo-moo there"
locationOfMoo = sentence.find("blah")
print("With .find")
print(locationOfMoo)
print(sentence[locationOfMoo:])

indexOfMoo = sentence.index("blah")
print("\n With .index")
print(indexOfMoo)
print(sentence[indexOfMoo])
