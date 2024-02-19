import csv
from plotly import offline
from plotly.graph_objs import Layout


lats, lons, brightnesses,dates = [], [], [], []
file_name = "data/world_fires_1_day.csv"
with open(file_name) as f:
     reader = csv.reader(f)
     next(reader)
     for row in reader:
          lats.append(row[0])
          lons.append(row[1])
          brightnesses.append(float(row[2]) / 100)
          dates.append(row[5])
          if len(dates) == 7_000:
               break
     
# mapping data
data = [{
     "type": "scattergeo",
     "lon": lons,
     "lat": lats,
     "text": dates,
     "marker":{
       "size": [3*br for br in brightnesses],
       "color": brightnesses,
       "colorscale": "viridis",
       "reversescale": True,
       "colorbar": {"title": "brightness"},
     },
     
}]
chart_layout = Layout(title= "fires burning in different location around the globe")
fig = {"data":data, "layout": chart_layout}
offline.plot(fig, filename="fires.html")