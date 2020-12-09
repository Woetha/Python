# Program asks a colour and modify it

colour = input("What is your favorite colour ")

# print first and third letter
for i in range (0, 2):
    print(colour[i], end="")
print()

print("This colour exist of", len(colour), "letters")
print()

# Prints every letter on a new line with the ASCII code
for letter in (colour):
    print(letter, "=", ord(letter))
print()

# Print every letter on a new line with extra symbols
i = 0
while i != len(colour):
    if i % 2: #2de, 4de, 6de, krijgen ** (even)
        print("**" + colour[i] + "**")
    else: #1ste, 3de, 5de, ... krijgen # (oneven)
        print("#" + colour[i] + "#")
    i += 1
