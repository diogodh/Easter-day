''' The Council of Nicaea in 325 AD defined Easter day as "Easter falls on the first Sunday following the first full moon after the vernal equinox (around March 21st). The vernal equinox is the moment when the sun crosses the celestial equator and day and night are of equal length.
In this script we will try to find the right day and month of Easter after 2020 AD'''

''' 
Moon orbit 29.53 days 
10th Jan at 19:21h (235.35h)
moon = 235.35 (29.53 dias)
moon_x = 235.35 + 708.72 * x
sunday = 96 + 168 * x
'''

# number of hours in a real (astrononimic) year (time earth takes to do a full orbit) 
year = 8765.8128

#hours from beguining of the year to the equinox
equinox = 1899.83

#input in that year you want to know the Easter day?
easter_year = int(input("Ano: "))

#Now let's go step by step. I believe its self explainable
dif_year = easter_year - 2020
hours_year = year + year * dif_year
equinox_year = equinox + year * dif_year

x= 0

# Calculate the lunar cycle until it reaches or exceeds the equinox of the given year
while True:
    moon = 235.35 + 708.72 * x
    if moon >= equinox_year:
        break
    x += 1

y = 0
# Calculate the Sunday cycle until it reaches or exceeds the lunar cycle
while True:
    sundayo = 96 + (168 * y)
    if sunday >= moon:
        break
    y += 1

day = sunday / 24
day_year = day - 365 * dif_year

# Determine the month and adjusted day of the year based on the calculated values
if day_year > 120.25:
    month = "May"
    day_year2 = day_year - 120.25
elif day_year > 90.25:
    month = "April"
    day_year2 = day_year - 90.25
else:
    month = "March"
    day_year2 = day_year - 59.25

# Print the predicted date of Easter in that year

print("Day ", int(round(day_year2)), "of ", month, "of ", year_easter)
