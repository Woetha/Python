# Program determines if the given word is a palindrome
# Made possible by Timo & Lennert <3

word = input("Give a word: ")
palindrome = True

# zolang 'i' in de lengte van het woord past / 2 (afgerond naar onder)

for i in range (int(len(word) / 2)):
    # print(woord[i] == woord[-i - 1]) #test of de eerste en laatste letter hetzelfde is, tweede en voorlaatste, etc...
    if word[i] != word[-i - 1]:
        palindrome = False
if palindrome == True:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

#lepel   l   e  p  e  l
#01234   -5 -4 -3 -2 -1