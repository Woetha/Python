with open("gegevens_werknemers.csv") as file:
    line = file.readline() # skip first line
    line = file.readline()
    record = line.split(";")

    last_name = input("Give your last name: ")
    ww = input("give your password: ")

    while line:
        if record[0] == last_name and record[1] == ww: # record2 werkt ni smh
            user_file = open(last_name + ".csv", "a") # opens file waar de user datums in kan schrijven
            # nog toe te voegen
            # ja of nee zeggen per datum
        else:
            print("skut")
        line = file.readline()
        record = line.split(";")