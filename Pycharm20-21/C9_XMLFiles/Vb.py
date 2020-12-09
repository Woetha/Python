import xml.etree.ElementTree as ET
xmlDoc = ET.parse("Files chapter 9/drugs.xml")
root = xmlDoc.getroot()

for child in root:
    print(child.tag, child.attrib)
print()
print("root[1].tag:", root[1].tag)
print("root[0][3].tag:", root[0][3].tag)
print("root[0][3].text:", root[0][3].text)
print("root[1][0].text:", root[1][0].text)
print("root[1][1][1].text:", root[1][1][1].text)
print("root[2][3].text:", root[2][3].text)
print()

# # It looks for the element named <leaflet>
# # Print the text of the first and the 4 child element of leaflet
# for leaflet in root.iter('leaflet'):
#     print(leaflet[0].text, ':', leaflet[3].text)

# # It searches for the element with <leaflet> in all child elements, even child of child
# for leaflet in root.iter('leaflet'):
#     print(leaflet[0].text) # Prints name
#     print('\t',leaflet[2].text) # Prints group
#     print('\t','pharmaceutical forms:')
#     for form in leaflet[1]: # looks for <form> in leaflet[1] (pharmaceutical_forms)
#         print('\t\t',form.text) # Prints the text of <form>

# # It searches for the element with <leaflet> in all child elements, even child of child
# for leaflet in root.iter('leaflet'):
#     name_drug = leaflet.find('name') # Searches the element <name> in <leaflet>
#     reason = leaflet.find('group') # Searches the element <group> in <leaflet>
#     print(name_drug.text)
#     print('\t', reason.text)
#     print('\t','pharmaceutical forms:')
#     for form in leaflet.find('pharmaceutical_forms'): # Searches <form> in <leaflet>
#         print('\t\t', form.text)

# # bigger example with iter and find
# for leaflet in root.iter('leaflet'):
#     reason = leaflet.find('group')
#     if reason.text == 'pain medication':
#         name_drug = leaflet.find('name')
#         print(name_drug.text)
#         for form in leaflet.find('pharmaceutical_forms'):
#             print('\t\t', form.text)

# # Searches for <leaflet> in the direct child of the current element (<drugs>)
# for leaflet in root.findall('leaflet'):
#     reason = leaflet.find('group')
#     if reason.text == 'pain medication':
#         name_drug = leaflet.find('name')
#         print(name_drug.text)
#         for form in leaflet.find('pharmaceutical_forms'):
#             print('\t\t', form.text)

# # Voorbeeld dat duidelijk maakt dat iter ook toelaat om in heel de boom te gaan kijken
# for info in root.iter('form'):
#     print('*',info.text)
