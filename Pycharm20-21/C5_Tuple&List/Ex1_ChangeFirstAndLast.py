# Program switches the first and last animal
# This is a list. I can change this later

animals = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]


print("Original list", animals)

# Gebruik een hulp variabele om 1 gegeven tijdelijk in op te slaan
last = animals[0]
# Zet het laatste gegeven op de eerste plaats (het eerste gegeven heb je hierboven opgeslagen in de hulp variabele
animals[0] = animals[-1]
# Zet het laatste gegeven (in de hulp variabele) op de laatste plaats
animals[-1] = last

print("After the switch", animals)