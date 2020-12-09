# Program makes a new text file from courses.csv
# The new text file is grouped by student number
# There is only one line per student
# The new file is "MadeFiles/Ex2_courses"

with open("Files chapter 8/courses.csv")as file:
    new_file = open("MadeFiles/Ex2_courses", "w")
    line = file.readline() # ignores first line
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        student_number = record[3]
        new_file.write(student_number + " " + record[5] + " " + record[4] + " " + record[1] + " (" + record[2] + " )")
        while line and record[3] == student_number:
            new_file.write(" " + record[1] + " (" + record[2] + " )")
            line = file.readline().rstrip()
            record = line.split(';')
        new_file.write("\n")
