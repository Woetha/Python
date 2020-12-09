# Program asks you for 10 numbers
# The numbers are tested on there last digit
# The program tells you how many integers end with the right digit

final_digit = int(input("What final digit do you want to check the numbers on: "))
right = 0
for i in range(10):
    number = int(input("Enter a number: "))
    if number % 10 == final_digit:
        right += 1
if right == 1:
    print("There is 1 number ending on", final_digit)
else:
    print(right, "out of", 10, "numbers end on", final_digit)


