# Program asks a word and print the 3 letters in the middle

word = input("Give a word: ")

# int is voor af te ronden -- eerste word zorgt dat de letter word weergegeven
print(word[int(len(word) / 2) - 1:int(len(word) / 2) + 2])