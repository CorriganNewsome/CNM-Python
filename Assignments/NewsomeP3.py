# NewsomeP3
# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: provides user capability to find fruit in a string

import string

# Use the list of fruits included with the assignment.

fruits = [
    "Apricot",
    "Asian Pear",
    "Avocado",
    "Banana",
    "Blackberries",
    "Blueberries",
    "Boysenberries",
    "Cactus Pear",
    "Cantaloupe",
    "Cherries",
    "Coconut",
    "Cranberries",
    "Figs",
    "Gooseberries",
    "Grapefruit",
    "Grapes",
    "Honeydew Melon",
    "Kiwifruit",
    "Limes",
    "Longan",
    "Loquat",
    "Lychee",
    "Madarins",
    "Malanga",
    "Mandarin Oranges",
    "Mangos",
    "Mulberries",
    "Nectarines",
    "Oranges",
    "Papayas",
    "Passion Fruit",
    "Peaches",
    "Pears",
    "Persimmons",
    "Pineapple",
    "Plums",
    "Pomegranate",
    "Prunes",
    "Quince",
    "Raisins",
    "Raspberries",
    "Rhubarb",
    "Strawberries",
    "Tangelo",
    "Tangerines",
    "Tomato",
    "Ugli Fruit",
    "Watermelon",
]
# Solve for single word fruit names first, for extra challenges solve for double word fruit names.

# Asks the user for a sentence.
userSentence = input("Please enter a sentence with a fruit in it: ")
titleCase = userSentence.title()

# remove punctuation
newSentence = titleCase.translate(str.maketrans("", "", string.punctuation))

# convert it to a list
sentenceList = list(newSentence.split(" "))
print(list(sentenceList))


set1 = set(sentenceList)
set2 = set(fruits)
result = list(set1 & set2)

if len(result) > 0:
    substitution = userSentence.split()
    substitution[sentenceList.index(result[-1])] = "Brussels Sprouts"
    print(f"\n\nI found {len(result)} fruits in your sentnece")
    print(f"Your fruits are {result}")
    print("Your final sentence with some brussels spouts is:", " ".join(substitution))
else:
    print("I found no fruits in your sentnece")
    print(f"Your final sentence is: {userSentence}")
