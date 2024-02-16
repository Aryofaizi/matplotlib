from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()


# roll the dice
results = []
for _ in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# set frequency
frequencies = []
for num in range(3, die_1.num_side + die_2.num_side + die_3.num_side +1):
    frequency = results.count(num)
    frequencies.append(frequency)
    
x_values = list(range(3,die_1.num_side + die_2.num_side + die_3.num_side +1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

title = "result of rolling 3 D6 dice 1000 times"
x_axis_config = {"title": "number", "dtick":1}
y_axis_config = {"title": "frequency of number"}
chart_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data":data, "layout":chart_layout}, filename="D6_D6_D6.html")