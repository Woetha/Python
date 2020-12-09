# Program checks if the last number is equal to the test
# Negative numbers won't be tested

number = int(input("Give a number: "))
if number < 0:
    print("A negative number will not be tested.")
else:
    final_digit = int(input("What final digit do you want to test with: "))
    last_number = number % 10
    if last_number == final_digit:
        print(number, "ends with", final_digit)
    else:
        print(number, "does not end with", final_digit)
print(last_number)