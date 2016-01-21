san_francisco_file = open("sanfrancisco_incidents_summer_2014.csv")
san_francisco_dates_file = open("sanfrancisco_dates.csv", "w")
first_line = True
for line in san_francisco_file:
    date = line.split(",")[4] + "\n"
    if not first_line:
        san_francisco_dates_file.write(date)
    first_line = False


seattle_file = open("seattle_incidents_summer_2014.csv")
seattle_dates_file = open("seattle_dates.csv", "w")
first_line = True
for line in seattle_file:
    date = line.split(",")[8][:10] + "\n"
    if not first_line:
        seattle_dates_file.write(date)
    first_line = False
