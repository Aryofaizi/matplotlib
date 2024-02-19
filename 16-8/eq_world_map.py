import json
from plotly import offline
from plotly.graph_objs import Layout



file_name = "data/eq_month.json"

with open(file_name,  encoding="utf8") as f:
     data = json.load(f)

    
lons, lats, mags, text_hovers = [], [], [], []
chart_title = data["metadata"]["title"]
for dict in data["features"]:
     lons.append(dict["geometry"]["coordinates"][0])
     lats.append(dict["geometry"]["coordinates"][1])
     mags.append(dict["properties"]["mag"])
     text_hovers.append(dict["properties"]["title"])
     
# mapping data
data = [{
     "type": "scattergeo",
     "lon": lons,
     "lat": lats,
     "text": text_hovers,
     "marker":{
       "size": [3* mag for mag in mags],
       "color": mags,
       "colorscale": "YlOrRd",
       "reversescale": False,
       "colorbar": {"title": "magnitudes"},
     },
     
}]
chart_layout = Layout(title= chart_title)
fig = {"data":data, "layout": chart_layout}

offline.plot(fig, filename="recent_earthquakes.html")