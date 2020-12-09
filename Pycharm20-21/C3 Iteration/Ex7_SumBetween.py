# Program gives the sum between 2 integers
# example : starting number = 5    final number = 7
# 5 + 5 = 10
# 10 + 6 = 16
# 16 + 7 = 23

starting_number = int(input("Give the starting number: "))
final_number = int(input("Give the final number: "))
sum = starting_number

if final_number < starting_number:
    print("The final number must be larger than the initial number")
else:
    if starting_number == final_number:
        print(starting_number)
    else:
        print("The sum of numbers between", starting_number, "till", final_number)
        for i in range (starting_number, final_number): # i = starting_number
            sum += i # i word bij de som opgetelt
            print("+", i, "-->", str(sum))
        print("+", final_number, "-->", str(sum + final_number))
