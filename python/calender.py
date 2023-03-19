# 22. Write a function where month and year are taken as arguments which returns the output
# with all the dates of saturdays occuring the month

def is_leap_year(year):
    if year%100 == 0:
        if year%400 == 0:
            return True
        return False
    elif year%4 == 0:
        return True
    return False

def list_of_saturday(year, month):
    month_code = {1:(1,31), 2:(4,28), 3:(4,31), 4:(0,30), 5:(2,31), 6:(5,30), 7:(0,31), 8:(3,31), 9:(6,30), 10:(1,31), 11:(4,30), 12:(6,31)}
    century_code = {15:0, 16:6, 17:4, 18:2, 19:0, 20:6, 21:4, 22:2}
    day_code = {0:'sat', 1:'sun', 2:'mon', 3:'tue', 4:'wed', 5:'thu', 6:'fri'}

    mc = month_code[month][0]
    cc = century_code[year//100]
    num_years_completed = year%100
    num_of_leap_year = num_years_completed//4

    num_of_days_in_month = month_code[month][1]

    leap_year = is_leap_year(year)
    if leap_year and month == 2:
        num_of_days_in_month += 1

    diff = 0
    if leap_year and month in (1, 2):
        diff = 1

    res = []
    for day in range(1, num_of_days_in_month+1):
        val = day + mc + cc + num_years_completed + num_of_leap_year - diff
        if day_code[val%7] == 'sat':
            res.append(day)

    return res

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))


print(f"list of staurday in {month}/{year} :",list_of_saturday(year, month))
