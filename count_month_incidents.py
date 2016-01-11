from datetime import datetime, date, time

f = open("seattle_dates.csv")
f = open("sanfrancisco_dates.csv")

dates_count_map = {}

for line in f:
    month, day, year = line[:10].split("/")
    d = date(int(year), int(month), int(day))
    key = d.month
    if not key in dates_count_map.keys():
        dates_count_map[key] = 0
    dates_count_map[key] = dates_count_map[key] + 1 

for key in dates_count_map.keys():
    print "{0},{1}".format(key, dates_count_map[key])

