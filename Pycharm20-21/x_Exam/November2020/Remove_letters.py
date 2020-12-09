# r0844999
# Hebberecht Wout
# 1ITF09

# NIET AF -- WERKT NIET

name = ["Wout", "Jana", "Leo", "Henry", "Michael"]

print(name)
print()



remove_letter = input("Enter the letter you want to remove. Press enter if you want to stop: ")

while remove_letter != "":
    for i in range(len(name)):
        word = name[i] # selecteerd appart woord
        for lenght_word in str(len(word)): # gaat elke letter van het woord af


            # verwijderd de gewenste letter
            if word == remove_letter:
                word = word.replace(remove_letter, "")

    print(name)
    remove = input("Enter the letter you want to remove. Press enter if you want to stop: ")

else:
    print()

