import random

random_number = random.randint(1, 10)
filename = "MadeFiles/table_" + str(random_number) + ".txt"
with open(filename, "w") as file:
    for i in range (1, 11):
        solution = i * random_number
        file.write(str(i) + "X" + str(random_number) + "=" + str(solution) + "\n")
