# r0844999
# Hebberecht Wout
# 1ITF09
name = ["Wout", "Jana", "Leo", "Henry", "Michael"]
print(name)
print()
remove_letter = input("Enter the letter you want to remove. Press enter if you want to stop: ")

while remove_letter != "":
    for i in range(len(name)):
        word = name[i]
        word = word.replace(remove_letter, "")
        name[i] = word
    print(name)
    remove_letter = input("Enter the letter you want to remove. Press enter if you want to stop: ")
else:
    print()
