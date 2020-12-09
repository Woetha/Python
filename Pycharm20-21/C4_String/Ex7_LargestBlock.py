# Program asks a string and checks for repeating letters
# 2 or more repeating letters are a block

word = input("Enter a word: ")
largest_block = 1
length_block = 1

# checks if i is equal to the next letter
for i in range (len(word)-1):
    if word[i] == word[i+1]: # checks if i is the same as the next letter
        length_block += 1
    else:
        length_block = 1
    # remembers the lenght in a differend variable if it is longer than largest_block
    if length_block > largest_block:
        largest_block = length_block

print("The length of the largest block in this text is", largest_block)