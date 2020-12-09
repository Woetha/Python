# Program tests if a party is awesome
# The party is good if there are 5 pizzas and 5 bottles of wine
# The party is fantastic if there are double the pizzas then bottles of wine (or visa versa)
# Other party's are stupid

pizza = int(input("How many pizzas are there: "))
wine = int(input("How many bottles of wine are there: "))
state_of_the_party = "stupid"

if pizza == wine * 2 or wine == pizza * 2:
    state_of_the_party = "fantastic"
else:
    if pizza >= 5 and wine >= 5:
        state_of_the_party = "good"

print("The party is", str(state_of_the_party))