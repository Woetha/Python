# Program reads a csv file and print out in a different order.
# It counts the measurements and calculate the average temperature of the date

with open("Files chapter 8/weather_2018 10.csv") as file:
    line = file.readline()
    line = file.readline()
    record = line.split(";")
    split_date = line.split(" ") # splits date and time
    while line:
        date = split_date[0]
        number_of_measurements = 0
        temp = 0
        while line and split_date[0] == date:
            temp += float(record[1])
            number_of_measurements += 1
            line = file.readline()
            record = line.split(";")
            split_date = line.split(" ")
        average_temp = round(float(temp) / int(number_of_measurements), 2)
        print(date.ljust(13), "Number of measurements = ", str(number_of_measurements).ljust(13), "average =", str(average_temp) )