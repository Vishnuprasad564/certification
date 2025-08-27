import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories = ['A','B','C']
values = [3,5,7]
plt.barh(categories,values,color=['red','green','blue'])
plt.title(" Horizontal Bar Plot")
plt.show()