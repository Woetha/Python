woord = input("Geef een woord: ")
klopt = True

# zolang 'i' in de lengte van het woord past / 2 (afgerond naar onder)
#
for i in range (int(len(woord) / 2)):
    #print(woord[i] == woord[-i - 1])
    if woord[i] != woord[-i - 1]:
        klopt = False

if klopt == True:
    print("Dit is een palindroom")
else:
    print("Dit is GEEN palindroom")


#lepel   l   e  p  e  l
#01234   -5 -4 -3 -2 -1