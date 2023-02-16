# Necessary module
import datetime

# Classes inside
#datetime.time
#datetime.datetime

# Creating a Date object
d1 = datetime.date(2012,8,23)
print(d1)
print(d1.strftime("%x"))


# Available fields
print(d1.month)
print(d1.strftime("%B"))

d2 = datetime.datetime.now()
print(d2)
print(d2.strftime("%Z"))

d3 = datetime.datetime(2022,2,16)

# Operations
diff = d3 - d2
print(diff)

# 1.Write a Python program to subtract five days from current date.
today = datetime.datetime.now()
print(today)

FiveDaysBefore = today.day - 20
#today.day = FiveDaysBefore
d2 = datetime.date(today.year, today.month, FiveDaysBefore)
print(d2)
