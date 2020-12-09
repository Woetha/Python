# Program asks you to guess the number
# It tells you if it is higher or lower and it counts your try's

number = 5
guesses = 1
your_guess = int(input("Give a positive number: "))

# Zolang je het nummer niet hebt geraden blijft de while afspelen
while your_guess != number:
    # guesses blijft optellen zolang je het juiste getal niet hebt geraden
    guesses += 1
    if your_guess > number:
        print("Lower!")
    else:
        print("Higher!")
    your_guess = int(input("Give a positive number: "))


print("You have guessed the number", str(number), "in", str(guesses), "turns.")
