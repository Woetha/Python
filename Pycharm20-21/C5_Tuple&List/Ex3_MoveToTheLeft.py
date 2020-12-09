# Program moves al the animals in the list to the left
# The first animal will be the last

#            0      1       2       3        4         5        6
animals = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("Before sliding", animals)
# Save the first animal in an extra var
help = animals[0]
# Delete the first animal. (move all the animals to the left)
animals.remove(animals[0])
# Add the first animal at the end
animals.append(help)

print("After sliding", animals)
