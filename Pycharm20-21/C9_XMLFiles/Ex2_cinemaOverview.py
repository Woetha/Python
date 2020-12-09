import xml.etree.ElementTree as ET
xmlDoc = ET.parse("Files chapter 9/cinemas.xml")

root = xmlDoc.getroot()
print("Bioscopen in Antwerpen")
for child in root.findall("bioscoopoverzicht"):

    # All var
    name = child[4].text
    street = child[5].text
    number = child[6].text
    postcode = child[7].text
    district = child[8].text
    # Prints
    print(name)
    print(street, number)
    print(postcode, district)
    print()
