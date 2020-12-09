numbers = {10, 90, 70, 56}
french_letters = set()

for sign in "éèçà":
    french_letters.add(sign)
vowels = set("aeioua")
squares = set(x**2 for x in range(10))

print(numbers)
print(french_letters)
print(vowels)
print(squares)