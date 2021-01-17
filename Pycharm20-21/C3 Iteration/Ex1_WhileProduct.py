# Program tests the product of multiple integers
# You need to give integers until you enter 0
# The program counts how many integers you multiply

total = 1
times = 0
product = int(input("Enter a number, stop by entering zero: "))
while product != 0:
    times += 1
    total *= product
    product = int(input("Enter a number, stop by entering zero: "))
print("The product of", times, "numbers is", total)
