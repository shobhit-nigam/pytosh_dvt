# fetching the date time

import datetime

d = datetime.datetime.now()

print(d)
print(d.strftime("%a"))

print(d.strftime("%a, %d of %b %Y"))


# import pywin32

# pywin32.SetSystemTime()
