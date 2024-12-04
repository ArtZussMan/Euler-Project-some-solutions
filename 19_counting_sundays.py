# Counting sundays
from datetime import date

date1 = date(1901, 1, 1)
date2 = date(2000, 12, 31)

date1_ord = date1.toordinal()  # returns the proleptic gregorian ordinal of a date
date2_ord = (
    date2.toordinal()
)  # this represents the number of days since January 1, 1 AD
cnt = 0

for d_ord in range(date1_ord, date2_ord):
    d = date.fromordinal(d_ord)
    if (d.weekday() == 6) and (d.day == 1):  # 6 represents Sundays
        cnt += 1

print(f"Number of Sunday 1st days is {cnt}")
