# Program makes a stair with numbers

for i in range(10, 21):
    for j in range(i, -1, -1): # j start op i(10) en telt af tot 0 --volgende trap-- j start op i(11) en telt af tot 0
        print(j, end=" ")
    print()