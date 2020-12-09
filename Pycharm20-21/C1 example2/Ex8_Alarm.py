current_time = int(input("Enter the current time: "))
wait = int(input("How long do you want to wait: "))

print("The alarm will go of at ", (current_time + wait) % 24)