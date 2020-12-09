# Program tests your BMI

weight = float(input("What is your weight"))
lenght = float(input("How tall are you: "))

bmi = (weight / lenght **2)* 10000
conclusion = "underweight"

if bmi < 18:
    conclusion = "underweight"
else:
    if 18 <= bmi < 25:
        conclusion = "normal weight"
    else:
        if 25 <= bmi < 27:
            conclusion = "slightly overweight"
        else:
            if 27 <= bmi < 30:
                conclusion ="moderated overweight"
            else:
                if 30 <= bmi <40:
                    conclusion = "obese"
                else:
                    if bmi >= 40:
                        conclusion = "sickly obese"
print("your bmi is", bmi)
print("you are", conclusion)