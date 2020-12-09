# Program calculates the series of Fibonacci
# it is a list starting with 0 and 1
# The next number is the sum of the 2 previous numbers
# Tell the program when you want to stop the list

first_number = 0
second_number = 1
third_number = first_number + second_number
stop = int(input("Up to which limit would you like to print the sequence of Fibonacci: "))
i = 0
while i < stop:
    print(first_number, second_number, third_number)


