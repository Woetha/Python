# Program makes a new list of the existing
# In the new list al the even numbers are in the first part of the list

random_numbers = [5, 8, 7, 9, 30, 8, 5, 63, 33, 45, 70]
# Empty lists
even_numbers = []
odd_numbers = []

print(len(random_numbers))

for number in random_numbers:
    if number % 2: # De oneven getallen
        odd_numbers.append(number)
    else: # De even getallen
        even_numbers.append((number))

# .extend werkt niet in print()
even_numbers.extend(odd_numbers)
print(random_numbers, "becomes", even_numbers)
