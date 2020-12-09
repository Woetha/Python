# Program asks a string and checks if 'in' is in it
# Specify if is is in the first or second place
# Don't use 'for' or 'while'

word = input("Enter a word: ")
position = word.find("in") # .find geeft '-1' als resultaat als het niet voorkomt

if position != -1:
    # checks if 'in' is in the first or second place
    if position in (0, 1):
        print("'in' appears in the first or second place of the word.")
    else:
        print("'in' appears in the word but not in the front")
else:
    print("'in' doesn't appear in the word")