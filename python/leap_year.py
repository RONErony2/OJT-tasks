# 9. Create a function is_leap_year that accepts a year and returns True if (and only if) 
# the given year is a leap year.

def is_leapYear(year):
    if year%100 == 0:
        if year%400 == 0:
            return True
        return False
    elif year%4 == 0:
        return True
    return False

year = int(input("Enter the year : "))

res = is_leapYear(year)

if res:
    print(f"{year} is Leap Year")
else:
    print(f"{year} is not Leap Year")