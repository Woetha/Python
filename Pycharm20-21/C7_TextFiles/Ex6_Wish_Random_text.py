import random
willekeurig = random.randint(1, 10)
string = "Files Chapter 7/wish" + str(willekeurig) + ".txt"

with open(string) as file:
    line = file.readline()
    print("Wish", str(willekeurig))
    print()
    while line:
        print(line.rstrip())
        line = file.readline()