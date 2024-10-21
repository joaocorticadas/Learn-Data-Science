import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(-10,11)
y_axis = x_axis ** 2

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plot of y = x^2")

plt.plot(x_axis, y_axis)
plt.savefig('graph.png')
