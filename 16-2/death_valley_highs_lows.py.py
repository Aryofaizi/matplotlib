import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = 'data/death_valley_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # get dates and high temperatures form this file.
    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
        
        
        
        
# Plot the high temperatures.        
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize = 20)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.ylim(10, 130)


plt.show()