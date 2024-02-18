import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = "data/death_valley_2018_simple.csv"


with open(file_name) as f:
    reader = csv.reader(f)
    header = next(reader)
    NAME = header.index("NAME")
    TMIN = header.index("TMIN")
    TMAX = header.index("TMAX")
    DATE = header.index("DATE")
    
    highs, dates, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[DATE], '%Y-%m-%d')
        try: 
            high = int(row[TMAX])
            low = int(row[TMIN])
        except ValueError :
            print(f"missing data for {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)
            

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, color="blue", alpha=0.1)

plt.title(f"Daily high and low temperatures - 2018\n{row[NAME]}", fontsize = 20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.ylim(10, 130)



plt.show()

        