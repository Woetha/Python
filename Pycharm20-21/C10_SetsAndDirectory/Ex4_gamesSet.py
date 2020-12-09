import xml.etree.ElementTree as ET

with open("Files Chapter 10/games.txt") as textfile:
    xmlDoc = ET.parse("Files Chapter 10/games.xml")
    root = xmlDoc.getroot()