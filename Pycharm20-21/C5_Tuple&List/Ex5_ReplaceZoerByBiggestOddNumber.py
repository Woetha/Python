# Program replaces all the 0 in the Tuple by the biggest odd number on the left side
# If there is no odd number the 0 remains

numbers = [42, 18, 0, 37, 0, 2, 19, 20, 5, 14]
# numbers = [42, 18, 17, 0, 2, 19, 0]
print("First it is ", numbers)

for index in range(len(numbers)-1):
    if numbers[index] == 0:
        # search largest_odd
        largest_odd = 0
        for i in range(index+1, len(numbers)-1):
            # Tests if the number is bigger than the last one and if the number is NOT odd (Niet deelbaar door 2)
            if numbers[i] > largest_odd and numbers[i] % 2 != 0:
                largest_odd = numbers[i]
        numbers[index] = largest_odd

print("Then it is", numbers)
