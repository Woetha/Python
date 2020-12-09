# Program counts the digits 6 and 0 in the integer
number = int(input("Give a number: "))
zeros = 0
sixes = 0
last = number

# i gaat elk getal appart af
for i in str(number):
    print(i)
    if int(i) == 6:
        sixes += 1
    elif int(i) == 0:
        zeros += 1

print("There are", str(zeros), "zeros and", str(sixes), "sixes")


# NIET AF