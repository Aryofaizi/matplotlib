import matplotlib.pyplot as plt

x_values = [x for x in range(1, 5_001)]
y_values = [x**3 for x in x_values]

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)


ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("X Values", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

ax.axis([0, 5500, 0,  150_000_000_000])
plt.show()



