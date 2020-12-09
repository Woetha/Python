three_digit_number = int(input("enter a three digit number please: "))

half_number = three_digit_number / 2
double_number = three_digit_number * 2
third_power_number = three_digit_number ** 3
tenfold_number = three_digit_number * 10

first_number = three_digit_number // 100
second_number = (three_digit_number // 10) % 10
third_number = three_digit_number % 10

print(half_number)
print(double_number)
print(third_power_number)
print(tenfold_number)
print(first_number)
print(second_number)
print(third_number)