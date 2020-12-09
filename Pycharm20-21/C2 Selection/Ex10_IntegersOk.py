# Program Tests if 2 int are OK
# They are ok if both numbers are between 30-40
# They are both equal to 65, 72, 83, 90

number1 = int(input("Number1: "))
number2 = int(input("Number2: "))
state = "Not ok"

if number1 in {65, 72, 83, 90} and number2 in {65, 72, 83, 90}: # Tests if numbers are equal to the following numbers
    state = "ok"
else:
    if 30 <= number1 <= 40 and 30 <= number2 <= 40: # Tests if numbers are between 30-40
        state = "ok"
print(state)

# Shorter version
if 30 <= number1 <= 40 and 30 <= number2 <= 40 or \
    number1 in {65, 72, 83, 90} and number2 in {65, 72, 83, 90}:
    print("Both numbers are OK")
else:
    print("Not OK")