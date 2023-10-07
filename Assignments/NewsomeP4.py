# NewsomeP3
# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: Utlizing dictionary in Python to translate a language.


# Creates a dictionary with common phrases in language a as the key and the translation in another language 2 as the values.
frenchPhrases = {
    "Comment allez vous": "How are you?",
    "Bonjour": "Hello",
    "Merci": "Thank You",
    "Je ne comprends pas": "I don't understand",
}
# Display a list of the phrases of language 1 to the user. Hint: use the .keys() method of the dictionary class.
print(" Select on of these phrases:", "    ".join(frenchPhrases.keys()))

# Ask the user to type in a phrase to translate.
sentence = input("Please enter a french phrase: ")

# Display the translation of that phrase to the user.
print("\nYour enlish tranlation is :", frenchPhrases[sentence])
