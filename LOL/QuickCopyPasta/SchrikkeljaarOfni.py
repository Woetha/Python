year = int(input("Give a year: "))

if year % 4 == 0 and year % 400 == 0 and year % 100 != 0:
    print(str(year), "is een schrikkeljaar")
else:
    print("skut")
