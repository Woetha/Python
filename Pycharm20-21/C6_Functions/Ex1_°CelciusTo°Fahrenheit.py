# Program converts Celcius to Farhenheit
tc = float(input("Degrees Celsius: "))

def conversion (tc):
    tf = 0
    tf = tc * (9/5) + 32
    return tf


print(tc, "°C = ", conversion(tc), "°F")
