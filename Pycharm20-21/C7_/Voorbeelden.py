# # Read line by line
with open('students.txt') as file:
    line = file.readline()
    while line:
        if line != '\n':
            print(line.rstrip())
        line = file.readline()
#
# # Read fields from record
# with open('students.txt') as file:
#     line = file.readline()
#     while line:
#         if line != '\n':
#             record = line.split(';')  #record is list met 3 elementen
#             print(record[2].rstrip(),':',record[0],record[1])
#         line = file.readline()
#
# # Read a file with numbers
# with open('students.txt') as file:
#     line = file.readline().rstrip()  #eerste lezen om smallest te kunnen initialiseren
#     record = line.split(';')
#     smallest = int(record[2])
#
#     line = file.readline().rstrip()   #tweede lijn lezen om te kunnen controleren
#     while line:
#         record = line.split(';')
#         number = int(record[2])
#         if number < smallest:
#             smallest = number
#         line = file.readline().rstrip()  #alle anderen lezen
# print('The oldest student is born in =',  smallest)
#
# # Read the file in a list and print every third list item
# with open('students.txt') as file:
#     lines = file.readlines()
#
#     for line in lines[::3]:
#         if line != '\n':
#             print(line, end='')
#
# # Read the file in a list, sort the list and print the fields of the record
# with open('students.txt') as file:
#     lines = file.readlines()
#     lines.sort()
#
#     for line in lines:
#         if line != '\n':
#             record = line.split(';')
#             print(record[2].rstrip(), record[0], record[1], sep='\t')
#
# # # Think twice before you use readlines!!!
# # # http://stupidpythonideas.blogspot.com/2013/06/readlines-considered-silly.html
