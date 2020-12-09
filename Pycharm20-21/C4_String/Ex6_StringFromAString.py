# Program asks a string to make a new string
# The letters are divided in groups of 3
# The first letter of a groups becomes the last letter
# If there is/are 1/2 letter(s) remaining it just adds them add the end

word = input("Give a word: ")
new_word = ""
i = 0

# repeats for as long as i is smaller than the lenght of the word - 2
while i < len(word) - 2:
    # new_word += second letter + third letter + first letter
    new_word += word[i+1] + word[i+2] + word[i]
    # next group of 3 letters
    i += 3

# adds the remaining letters.
new_word += word[i:]
print(new_word)