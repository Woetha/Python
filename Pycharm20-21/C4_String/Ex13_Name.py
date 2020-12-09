# Program asks for your name and gives you a pop-up
# In the pop-up you can select how you want your name to be written (lower case, uppercase, both)

name = input("Give your name: ")
print()

print("Menu")
print("****")
print("U Uppercase")
print("L Lowercase")
print("A Alternate")
print()

choise = input("Make a choise (U-L-A): ")

if choise == "U" or choise == "u":
    print(name.upper())
if choise == "L" or choise == "l":
    print(name.lower())
if choise == "A" or choise == "a":
    i = 0
    while i != len(name):
        if i % 2:
            print(name[i].upper(), end="")
        else:
            print(name[i].lower(), end="")
        i += 1
