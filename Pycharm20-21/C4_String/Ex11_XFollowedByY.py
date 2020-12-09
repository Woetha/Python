# Program tests if there is an X in the sentence
# If there is an X it looks for an Y
# Every X needs to be followed by an Y
# Multiple x'es can be followed by a single y

text = input("Enter a text: ")
letter = ""
y = 0
x = 0

# Checks the whole word
for i in range(len(text)):
    if text[i] == "x" or text[i] == "X": # Checks if letter is x
        x += 1
        if text[i] == "y" or text[i] == "Y": # If there is an x, check for a y
            y += 1
    else:
        i += 1

if x == y and x != 0:
    print("In this text every x is followed by a y.")
else:
    print("In this text not every x is followed by a y")
# Doesn't work
