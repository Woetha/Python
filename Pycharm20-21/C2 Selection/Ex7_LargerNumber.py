# Program tests for the biggest number
# If a number is negative you make it positive
# If both numbers are equal the answer is 0
# If both numbers are divisible by 5 the answer is "The smaller of two numbers"

number1 = int(input("Number1: "))
number2 = int(input("Number2: "))
bigger = number1

# Make positive
if number1 < 0:
    number1 *= -1
if number2 < 0:
    number2 *= -1

# Checks if the numbers are dividible by 5
divide1 = number1 % 5
divide2 = number2 % 5
if divide1 == 0 and divide2 == 0:
    print("The smaller of two numbers")

# Checks if numbers are equal
else:
    if number1 == number2:
        bigger = 0
    else:
        if number2 > bigger:
            bigger = number2
    print("The answer for the numbers", str(number1), "and", str(number2), "=", bigger)

