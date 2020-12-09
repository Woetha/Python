import xml.etree.ElementTree as ET
# use this file
xmlDoc = ET.parse("Files chapter 9/plants.xml")
# Find the root <catalog> in this case
root = xmlDoc.getroot()
count = 0

# Lets you look in the child elements of "plant"
for common in root.findall("plant"):
    if common[3].text == "SUN": # oefb - Ony show plant that are best in the sun
        count += 1
        name = common[0].text # .text to print the words inside
        botanical = common[1].text
        print("plant", str(count), ":", name, " (" + botanical + ")")
