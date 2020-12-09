# Program reads a number of intigers
# To stop the program enter 0
# At the end, it will tell you the difference between the biggest and the smallest number
# If no number is entered print "no numbers entered"

number = int(input("Enter a number: "))
highest = number
lowest = number

if number == 0:
    print("No number entered")
else:
    while number != 0:
        if number < lowest:
            lowest = number
        else:
            highest = number
        number = int(input("Enter a number: "))
    print("The lowest number is", lowest, "and the heighest nubmber is", highest)
    print("The difference is", (highest - lowest))