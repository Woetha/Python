# Program reads the file 'student.txt' and count how many records are in there
# It also reads how many "z" are in the file

name_count = 0
zets = 0
with open('Files Chapter 7/first_names.txt') as file:
    line = file.readline()
    while line:
        if line != '\n':
            print(line.rstrip())
            name_count += 1
        line = file.readline()
        if "z" in line or "Z" in line:
            zets += 1
    print("There are", name_count, "first names in the file.")
    print(zets, "of with contain a Z")
