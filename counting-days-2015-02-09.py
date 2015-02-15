from datetime import date

print("Please provide desired date as: yyyy mm dd")
text = raw_input("Date: ")

year, month, day = text.split()

year = int(year)
month = int(month)
day = int(day)

today = date.today()
calc_date = date(year, month, day)

delta = calc_date - today

print "There are", abs(delta.days), "day(s) between", today, "and", calc_date
