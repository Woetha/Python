yes = int(input("How many voted yes: "))
no = int(input("How many voted no: "))
blank = int(input("How many didn't vote: "))

total = yes + no + blank
#percentage berekenen --> stemmen / totaal * 100
percentage_yes = yes / total * 100
percentage_no = no / total * 100
percentage_blank = blank / total * 100

print("YES: " + str(percentage_yes) + "%")
print("NO: " + str(percentage_no) + "%")
print("BLANK: " + str(percentage_blank) + "%")