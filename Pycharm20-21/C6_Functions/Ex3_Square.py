# Programma vraagt een symbool en getal
# Het print het symbool het gegeven aantal keren af
# Het programma stopt als je ENTER ingeeft i.p.v. een getal

def press_square(number, symbol):
    for i in range(number):
        return(symbol * number)


symbol = input("Which character must be used to form a square (ENTER = stop): ")

if symbol == "":
    print()
else:
    while symbol != "":
        number = int(input("Number of characters per line and number of lines: "))
        for i in range(number):
            print(press_square(number, symbol))
        symbol = input("Which character must be used to form a square (ENTER = stop): ")
