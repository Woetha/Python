# r0844999
# Hebberecht Wout
# 1ITF09


print("Enter 5 codes consisting of a letter and a number")
good = 0

for i in range(1, 6):
    code = input(str(i) + ")")
    letter = int(ord(code[0]))
    number = int(code[1:])
    if letter == number:
        good += 1
    else:
        print(letter, "<-->", code[1:])

if good == 1:
    print("1 code was OK")
else:
    print(good, "codes were OK")
