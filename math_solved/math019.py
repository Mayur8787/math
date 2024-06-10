import calendar

year = 1901
month = 1
count = 0
while year < 2001:
    if calendar.weekday(year,month,1) == 6:
        count += 1
    month += 1
    if month > 12:
        year += 1
        month = 1
print(count)