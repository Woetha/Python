# Program searches for the shortest verse in the text file.

with open("Files Chapter 7/irish_song.txt")as file:
    line = file.readline()
    shortest_length = len(line.rstrip())
    shortest_verse = line.rstrip()
    while line:
        if line != "\n":
            if len(line) < shortest_length:
                shortest_length = len(line.rstrip())
                shortest_verse = line.rstrip()
            line = file.readline()
    print("The shortest line has", shortest_length, "characters.")
    print(shortest_verse)
