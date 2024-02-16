from matplotlib import pyplot as plt

from die import Die

die = Die()

# rolling die
results = []
for _ in range(1000):
    result = die.roll()
    results.append(result)
    
# frequency for each side number
frequencies = [results.count(num) for num in range(1,die.num_side+1)]

x_values = list(range(1, die.num_side+1))

# create chart
plt.style.use("bmh")
fig, ax = plt.subplots()


#set x,y axis values.
ax.plot(x_values, frequencies)

# customize plot
ax.set_title("result of rolling D6 dice", fontsize=24)
ax.set_xlabel("side numbers", fontsize=14)
ax.set_ylabel("frequency of side numbers", fontsize=14)

plt.show()


