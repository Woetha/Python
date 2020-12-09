
vowels = ('a', 'e', 'o', 'u', 'i')

with open("Files Chapter 7/hamlet_remove_vowels.txt", "w+") as file:
        line = file.readline()
        while line:
                if vowels in line:
                        line.replace(vowels, "")
                print(line)
                line = file.readline()
