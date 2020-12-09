# Het programma vraagt de exchange rate en het aantal euros dat je hebt
exchange_rate = float(input("Current dollar rate: "))
euro = float(input("Your amount in Euros: "))


def convert(euro, exhange_rate):
    dollar = euro * exhange_rate
    return dollar


print("€", euro, "= $", convert(euro, exchange_rate))
