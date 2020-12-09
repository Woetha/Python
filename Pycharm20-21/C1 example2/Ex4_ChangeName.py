name1 = input("Naam 1: ")
name2 = input("Naam 2: ")
print("Before changing: ", name1, name2)

help = name1
name1= name2
name2 = help

print("After changing: ", name1, name2)