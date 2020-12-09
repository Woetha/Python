# Program tells you in wich group you belong

age = int(input("Your age is: "))
section = "Beavers"

if 6 <= age <= 7:
    section = "Beaver"
if 8 <= age <= 10:
    section = "Cub"
if 11 <= age <= 13:
    section = "Scout"
if 14 <= age <= 18:
    section = "Explorer"
if age >= 18 :
    section = "Leader"

print("You are a", section)