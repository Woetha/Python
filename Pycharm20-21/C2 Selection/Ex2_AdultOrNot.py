# Program test if you're an adult or not (+18)

current_year = 2020
year_of_birth = int(input("Enter your year of birth: "))
age = current_year - year_of_birth

print("Your age is ", int(age))
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
