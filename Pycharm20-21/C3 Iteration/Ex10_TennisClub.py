# Program calculates the fee for club members based on age
# 12 years or younger = €20
# Between 12 years and 18 years = €50
# Older than 18 = €95
# If you are a member for 5 years or more you get a 10% discount

for i in range(4):
    print("Information for member", i+1)
    name = input("Name: ")
    age = int(input("Age: "))
    member = int(input("Member for how many years: "))
    if age < 12:
        fee = 20
    else:
        if 12 < age <= 18:
            fee = 50
        else:
            if age > 18:
                fee = 95
    if member >= 5:
        fee /= 1.1
    print("Member fee for", name, "=", int(fee))
    print()
