# Program makes a new Tuple from an existing Tuple
# The new Tuple exist of all the numbers after 4
# This is a Tuple. I can't change this later

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Position   0  1  2  3  4  5  6  7  8
if 4 not in numbers:
    print("There is no #4 in this tuple.")
else:
    numbers_after_four = (numbers[numbers.index(4) + 1:])# De posities na de #4
    print(numbers, "becomes", numbers_after_four)
