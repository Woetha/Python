# Program asks a word and prints the first letter and the lasts few letters

word = input("Give a word: ")
number = int(input("Give a number: "))

# print eerste letter + print laatste aantal letters v/h woord aangegeven door number
print(word[0] + word[-number:])