with open("Files Chapter 7/playlist.txt") as file:
    line = file.readline()
    record = line.split(";")
    print("Playlist")
    for lines in line:
            print(record[0], "\t", record[1], "(" + record[2].lower() + ")")
            line = file.readline()
            record = line.split(";")
