
with open("Files chapter 8/classrooms.txt") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        classroom = record[2]
        student_count = 0
        print(classroom)
        while line and record[2] == classroom:
            student_count += 1
            print('  ' + record[1] + " " + record[0])
            line = file.readline().rstrip()
            record = line.split(';')
        print("Number of students in classroom", classroom, "=", student_count)
