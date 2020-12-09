# Program asks for some text and puts every letter in the list (no spaces)
# It prints the list in 3 different ways

text = input("Enter a text: ")
letters = []
for i in range (int(len(text))):
    if text[i] != " ":
        letters += text[i]
# Ex6 a
letters.sort()
print(letters)
print(*letters)
print(*letters , sep="\t")

# Ex6 b
# # Only put letters in the lists if that letter is not already in the list
# used_letters = []
#     if text[i] not in (used_letters):
#         used_letters += text[i]
# used_letters.sort()
# print(used_letters)
# print(*used_letters)
# print(*used_letters , sep="\t")


