# r0844999
# Hebberecht Wout
# 1ITF09

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

between = []

if first_number == second_number:
    print("Sorry, we can not create a list for you.")
else:
    if first_number > second_number:
        remember = first_number
        first_number = second_number
        second_number = remember

    for i in range (first_number, second_number):
        between.append(i)
    print(between)
