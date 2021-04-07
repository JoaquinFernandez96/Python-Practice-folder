import matplotlib.pyplot as plt
import numpy as np

e = 1504170715041707
mod = 4503599627370517
tot = e
min = e
max = e

v_temp = []
min_temp = []
max_temp = []
while True:
    if min == 1:
        break
    v = min + max
    print(v, min, max)
    v_temp.append(v)
    min_temp.append(min)
    max_temp.append(max)
    v %= mod
    if v > max:
        max = v
    if v < min:
        min = v
        tot += min
print("TOTAL:", tot)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(v_temp[5:15], label="V")  # Plot some data on the axes.
ax.plot(min_temp[5:15], label="min")  # Plot more data on the axes...
ax.plot(max_temp[5:15], label="max")  # ... and some more.
ax.set_xlabel("x label")  # Add an x-label to the axes.
ax.set_ylabel("y label")  # Add a y-label to the axes.
ax.set_title("eulercoin")  # Add a title to the axes.
ax.legend()  # Add a legend.
