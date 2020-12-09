# Program asks for your name and the distance to school
# It puts your names in a list and your distances in a list
# It tells you who lives the fartest from school and the average distance

print("Enter your name and the distance to school.")
print("Type stop when you want to close the entry")
names = []
distances = []

name = input("Your name: ")
while name != "stop":
    names.append(name)
    distance = float(input("Distance to school: "))
    distances.append(distance)
    name = input("Your name: ")

if len(names) < 1:
    print()
else:
    print()
    print("overview")
    for i in range (len(names)):
        print(names[i], "\t", distances[i])
    average = sum(distances) / len(distances)

    print()
    print("the average distance is", average)