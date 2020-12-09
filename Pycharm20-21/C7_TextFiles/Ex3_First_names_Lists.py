# NIET AF

name_list = []

with open('Files Chapter 7/first_names.txt') as file:
    line = file.readline()
    while line:
        if len(name_list) != 10:
            name_list.append(line.rstrip())
        else:
            print(name_list)
            name_list = []
            name_list.append(line.rstrip()) # first name of the next row
        line = file.readline()
    print(name_list)
