# Program prints a new list, double the lenght than the first one with all 0
# Except the last element. This is the last element of the first list

first = [2, 4, 5, 9, 8]
second = []

# The lenght of the list - 1 (the last element)
for i in range (len(first) -1):
    second += "0" * 2 # Double the lenght
second.append("0")
second.append(first[-1])
print(first)
print(second)