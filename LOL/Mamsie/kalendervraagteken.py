import calendar

c = calendar.TextCalendar (calendar.MONDAY)
str = c.formatmonth(2025, 4)
j = 1
print(str)
print()
for name in calendar.month_name:
    print(name)
    for j in range (31):
        print(j)