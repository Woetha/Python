# Program reads 2 files and counts the different names
# It prints the names if they are in 1ITF and 2ITF

with open("Files Chapter 10/first_names1ITF.txt") as file1:
    file2 = open("Files Chapter 10/first_names2ITF.txt")
    line1 = file1.readline().strip()
    line2 = file2.readline().strip()
    names1 = set()
    names2 = set()
    while line1:
        names1.add(line1)
        line1 = file1.readline().strip()
    while line2:
        names2.add(line2)
        line2 = file2.readline().strip()

name1_2 = names1.intersection(names2)
print("In 1ITF there are", len(names1), "different first names.")
print("In 2ITF there are", len(names2), "different first names.")
print("These are the", len(name1_2), "first names appearing in 1ITF and 2ITF")
# for name in name1_2:
#     print(name)  # this set is never the same

# oef b
names_list = list(name1_2)
names_list.sort()
for name in names_list:
    print(name)  # this set is always the same
