
# Doesn't work

with open("../C3 Iteration/Ex10_TennisClub.py")as program:
    file = open("MadeFiles/Ex10_Program_Without_Numbering.txt", "w")
    solution = []
    count = 1
    lines = program.readline()
    while lines:
        file.write(str(count) + ") " + str(lines))
        count += 1
        lines = program.readline()
