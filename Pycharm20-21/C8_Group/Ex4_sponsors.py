
with open("Files chapter 8/sponsors.txt") as file:
    line = file.readline().rstrip()
    record = line.split("*")
    print("Overview gifts")
    print("Number".ljust(10) + "Sponsor")
    list = []
    while line:
        number = (record[0])
        if number not in list:
            list.append(number)
        print(list)

        line = file.read()
        record = line.split("*")
