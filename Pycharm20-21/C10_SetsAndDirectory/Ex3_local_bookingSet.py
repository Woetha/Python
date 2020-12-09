# Program reads the file and print every classroom 1 time

with open("Files Chapter 10/local_booking.txt") as file:
    line = file.readline().strip()
    record = line.split(";")
    classrooms = set()
    while line:
        classrooms.add(record[3])
        line = file.readline().strip()
        record = line.split(";")

    print("Classrooms:")
    for room in classrooms:
        print(room)
