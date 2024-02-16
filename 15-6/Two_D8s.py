from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die_1 = Die(8)
die_2 = Die(8)

# calculate the result
results = []
for _ in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
frequencies = []
# count result
for num in range(2, die_1.num_side + die_2.num_side +1):
    frequency = results.count(num)
    frequencies.append(frequency)

#visualize chart
x_values = list(range(2, die_1.num_side + die_2.num_side +1))
y_values = frequencies

data = [Bar(x=x_values, y=y_values)]

title = "Result of rolling two D8 Dice 1000 times."
x_axis_config = {"title": "sides", "dtick":1}
y_axis_config = {"title": "frequencies"}
chart_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data":data, "layout": chart_layout}, filename="D8_D8.html")


