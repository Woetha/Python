# Program makes multiple tests with 3 numbers
# If the 3 numbers are equal to 2, then the result is 10
# If all 3 are equal but not equal to 2 then the result is 5.
# If the numbers b and c are different from a then the result is 1
# In all other cases the result is 0.

a = input("Number1 (0, 1, 2) ")
b = input("Number2 (0, 1, 2) ")
c = input("Number2 (0, 1, 2) ")
answer = 0


if a == 2 and b == 2 and c == 2: # Tests if al numbers are equal to 2
    answer = 10
    if a == b == c != 2: # Tests if all numbers are equal. But are not 2
        answer = 5
if b == c and a != b and a != c: # Tests if b and c are equal to each other but not to a
    answer = 1
print(answer)
