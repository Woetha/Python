# Program asks for your score
# It will put them in a list and order them form lowest to highest
# It will give you the average score and how many times you entered a score
# End by entering -1

print("Enter the score for the test. Use -1 if you want to finish")
score = []
times = -1
total = 1
while score != -1:
    # float(input), anders zal python dit zien als een str en geen getal en krijg je een oneindige loop
    score = int(input("Score: "))
    times += 1
    total += score

# NIET AF
# Lijst niet gesorteerd

average = total / times
print("The average of these", times, "scores =", average)