# programs print '..' between each number until 0

number = int(input("Enter a number: "))
while number != 0: # tot en met 1
    print(number, "", sep='..', end='')
    number -= 1
print("0")