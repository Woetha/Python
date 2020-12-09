# Program asks for 5 words and puts them in reverse order
# First word is Last, Second word is pre-Last, ...

i = 1
sentence = ""
for i in range(1, 6):
    # Komma gaat alleen maar bij input. Plustekens gaan alleen maar met strings.
    word = input("Enter word " + str(i) + " : ").capitalize()
    # Adds the new word to 'sentence' and keeps the previous words
    sentence = word + " " + sentence
print("The words in reversed orders are:")
print(sentence)