import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([40, 90, 120, 190, 205, 215, 250])

plt.plot(x, y, marker = "o",
         markersize = 5)
plt.title("Times I've Dry Beat to Miles Last Week")
plt.ylabel("Times Beated")
plt.xlabel("Days of the week")
plt.show()
