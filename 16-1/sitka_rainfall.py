import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = "data/sitka_weather_2018_simple.csv"
data = []
dates = []
with open(file_name) as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for row in reader:
        try:
            data.append(float(row[3]))
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        except:
            print("missing data")
        
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, data)
fig.autofmt_xdate()

plt.title("daily rainfall in sitka", fontsize=18)
plt.xlabel("dates", fontsize=14)
plt.ylabel("rainfall amount", fontsize=14)
plt.tick_params(axis="x", labelsize=10)
plt.yticks(rotation = 25)
plt.ylim(min(data) ,max(data))
plt.show()
