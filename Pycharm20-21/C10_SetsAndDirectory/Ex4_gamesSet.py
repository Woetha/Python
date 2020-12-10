import xml.etree.ElementTree as ET

# Program reads a text-file and a XML-file
# It looks for the game-types and puts them in a set
# Then prints them in 3 groups

type_textfile_set = set()
type_xmlfile_set = set()
type_both_set = set()

# Text-file
with open("Files Chapter 10/games.txt") as textfile:
    line = textfile.readline()
    record = line.split(",")

    while line:
        game_type = record[7].replace("'", "")
        type_textfile_set.add(game_type)
        line = textfile.readline()
        record = line.split(",")

# XML-file
xmlDoc = ET.parse("Files Chapter 10/games.xml")
root = xmlDoc.getroot()
for game in root.findall("game"):
    type_xmlfile_set.add(game[1].text)
type_both_set = type_textfile_set.intersection(type_xmlfile_set)

# Prints
print("In the text-file are", len(type_textfile_set), "types of games")
print("In the XML-file are", len(type_xmlfile_set), "types of games", "\n")
print("The types that occur in both files:")
print(type_both_set, "\n")
print("The types that occur in the text-file:")
print(type_textfile_set, "\n")
print("the types that occur in the XML-file:")
print(type_xmlfile_set.difference(type_both_set))

