from plotly.graph_objs import Bar, Layout
from plotly import offline

from random_walk import RandomWalk


rw = RandomWalk(1_000)
rw.fill_walk()
print(rw.x_value, rw.y_value)

data = [Bar(x=rw.x_value, y=rw.y_value)]

title = "Result of random walk"
x_axis_config = {"title": "x coordinate", "dtick":1}
y_axis_config = {"title": "y coordinate"}
chart_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data":data, "layout":chart_layout}, filename="random_walk.html")
