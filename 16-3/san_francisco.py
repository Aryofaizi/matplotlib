import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = "data/san_francisco.csv"


with open(file_name) as f:
    reader = csv.reader(f)
    header = next(reader)
    
    highs, dates, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try: 
            high = int(row[4])
            low = int(row[5])
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

plt.title("Daily high and low temperatures - 2018\nSan Francisco", fontsize = 20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.ylim(10, 130)



plt.show()

        