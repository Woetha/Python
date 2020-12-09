word = input("Enter a string: ")
new_word = word
print()
previous_letter = ""
next_letter = ""
i = 0
for i in range (len(word) - 1):
    if word[i] == "*":
        previous_letter = word[i - 1]
        next_letter = word[i + 1]
        word = word.replace("*", "")
        word = word.replace(previous_letter, "")
        word = word.replace(next_letter, "")
    else:
        print("")

print(word)
# werkt niet
