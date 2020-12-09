# Program prints the text file from bottom to top

with open('Files Chapter 7/first_names.txt') as file:
    lines = file.readlines()

    for line in lines[-1:0:-1]:
        if line != '\n':
            print(line, end='')