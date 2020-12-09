sentence = "hard work pays of"
print(sentence)

#zet alle letters in hoofletter. Moet in een print() gebruikt worden
sentence.upper()
print(sentence)
print(sentence.upper())

#Zit een letter/woordgroep in de zin
if "h" in sentence:
    print("yes")
else:
    print("No")

#Telt het aantal "r" in de zin
sentence_count = sentence.count("r")
print(sentence_count)

#Op welke plaats staat "w"
sentence_find = sentence.find("w")
print(sentence_find)

