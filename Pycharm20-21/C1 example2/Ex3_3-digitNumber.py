number = int(input("Enter a 3-digit number: "))
half = number / 2
double = number * 2
third_power = number ** 3
tenfold = number * 10
first_number = number // 100
second_number = (number - first_number * 100) // 10
third_number = number - (first_number * 100) - (second_number * 10)

#Andere oplossing in 3digitnumber2

print("Half = " + str(half))
print("Double = " + str(double))
print("Third power = " + str(third_power))
print("Tenfold = " + str(tenfold))
print("First number = " + str(first_number))
print("Second number = " + str(second_number))
print("Third number = " + str(third_number))