import xml.etree.ElementTree as ET
xmlDoc = ET.parse("Files chapter 9/jobs.xml")

root = xmlDoc.getroot()
count = 0

print("Overview IT vacancies:")
print()
for contact in root.iter("contact"):
    email = contact[1].text
    for company in root.iter("company"):
        name = company[0].text
        for vacancy in root.iter("vacancy"):
            if vacancy[0].attrib == "IT":
                positions = vacancy[0].text
                print(positions)

            print(vacancy[0].tag, vacancy[0].attrib)
