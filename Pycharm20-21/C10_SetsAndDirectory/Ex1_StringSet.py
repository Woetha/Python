# Program asks to give a text consisting of letters and numbers
# it puts the letters and numbers in separate sets.

string = input("Enter a random text of letters and numbers: ")
# Make sets
letters_set = set()
numbers_set = set()
# Reads one symbol at the time
for i in range(int(len(string))):
    letters = ""
    letters += string[i]
    if letters.isdigit(): # check for digits (numbers)
        numbers_set.add(letters)
    else:
        letters_set.add(letters)
print("The numbers:")
print(numbers_set)
print("The letters:")
print(letters_set)
