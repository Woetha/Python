# Program removes * and the letter before and behind *
# You may assume * doesn't appear on the first or last place

word = input("Enter a string: ")
while "*" in word:
    place = word.find("*")  # find *
    word = word.replace(word[place - 1:place + 2], "")  # removes * and the letter before and after (replace with blank)
print(word)
