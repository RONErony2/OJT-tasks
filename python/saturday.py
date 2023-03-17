# 22. Write a function where month and year are taken as arguments which returns the output
# with all the dates of saturdays occuring the month

import calendar

# mon - 0, tue - 1, wed - 2, thu - 3, fri - 4, sat - 5, sun - 6

# 1st approach
def list_of_saturday(month,year):
    num_days = calendar.monthrange(year, month)[1] # (2, 31)
    saturday = []
    for day in range(1,num_days+1):
        weekday = calendar.weekday(year, month, day)

        if weekday == 5:
            saturday.append(day)
    return saturday

list = list_of_saturday(3,2023)
print(list)


# 2nd approach

cal = calendar.Calendar()

def list_of_saturday(month,year):

    saturday = []
    for day in cal.itermonthdays2(year, month):
        print(day)
        if day[0] != 0 and day[1] == 5:
            saturday.append(day[0])
    return saturday

print(list_of_saturday(3,2023))