# Program says when you should pick up your phone
# You never pick up if you're asleep
# In the morning you only pick up if your mother calls

# Must be done with Booleans

is_asleep = False
is_morning = True
is_mother = True


if is_asleep: # Checks if it is True
     print("I'm not answering the phone")
else:
    if is_morning and is_mother: # Checks if both are True
        print("I pick up the phone.")
    else:
        if is_morning or is_asleep: # Checks if one is True
            print("I never pick up the phone.")
