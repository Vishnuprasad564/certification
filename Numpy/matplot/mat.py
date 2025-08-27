import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,100)
y = np.tan(x)
plt.plot(x,y, color='black', linestyle='--', marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()