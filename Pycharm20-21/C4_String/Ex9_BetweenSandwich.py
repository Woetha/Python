# Program asks for a sentence to find what is between your sandwich
# Don't use 'for' or 'while'

sentence = input("What did you eat for lunch: ")
first_position = sentence.find("sandwich")# .find geeft '-1' als resultaat als het niet voorkomt
if first_position != -1:
    # Sandwich is 8 letters long
    # Find the second sandwich
    new_text = sentence[first_position + 8:]
    second_position = new_text.find("sandwich")

    if second_position != -1:
        # between_sandwich start vanaf achter de eerste sandwich en
        # stopt voor de eerste letter van de tweede sandwich
        between_sandwich = new_text[0:second_position]
        print("You have", between_sandwich, "between your sandwich")