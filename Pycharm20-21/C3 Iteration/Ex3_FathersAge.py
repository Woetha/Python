# Program tells when your father is twice your age

my_age = int(input("How old are you: "))
fathers_age = int(input("How old is your father: "))
years = 0
answer = True

# Keep testing until my father is twice my age
while fathers_age != my_age * 2:
    if fathers_age <= my_age or fathers_age > 110: # If it is not possible
        print("This is not possible")
        fathers_age = my_age * 2
        answer = False # Stops the other answer
    else:
        fathers_age += 1
        my_age += 1
        years += 1
if answer:
    print("Within", years, " Your father will be twice your age.")
    print("Your father will be", fathers_age, "and you will be", my_age, "years.")