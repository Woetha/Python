
with open("Files Chapter 7/contacts.csv") as file:
    line = file.readline()
    boys = 0
    girls = 0
    boys_list = []
    girls_list = []

    while line:
        record = line.split(';')
        if record[3] == "M\n":
            boys += 1
            boy_name = record[1] + " " + record[0]
            boys_list.append(boy_name)
            boys_list.sort()
        else:
            girls += 1
            girl_name = record[1] + " " + record[0]
            girls_list.append(girl_name)
            girls_list.sort()
        line = file.readline()

    print(girls, "girls:")
    for girl in girls_list:
        print("\t", girl)
    print(boys, "boys:")
    for boy in boys_list:
        print("\t", boy)
