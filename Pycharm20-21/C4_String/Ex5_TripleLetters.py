# Program tests if a letter is repeated 3 times in a word
# Made possible by Timo & Lennert <3

word = input("Give a word: ")
triple = 0
print(len(word))
print(len(word) - 2)
for i in range (len(word) - 2):
    # Tests if the first letter is the same as the second an third letter
    if word[i] == word[i + 1] and word[i] == word[i + 2]:
        triple += 1

if triple == 0:
    print("There are no triples in this word")
else:
    if triple == 1:
        print("There is", triple, "triple in this word")
    else:
        print("There are", triple, "triples in this word")


#rop
#012