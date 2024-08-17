

# using ternary operator
year = int(input("Enter a year: "))
leap_year = "Leap year" if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0 else "Not a Leap year"
print(leap_year)

# using calender module
import calendar
year1 = int(input("Enter a year: "))
leap_year1 = "Leap Year" if calendar.isleap(year1) else "Not a Leap year"
print(leap_year1)