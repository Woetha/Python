woord = input("geef een woord ")
#int is voor af te ronden -- eerste woord zorgt dat de letter word weergegeven
print(woord[int(len(woord)/2) - 1] + woord[int(len(woord)/2)] + woord[int(len(woord)/2) + 1])