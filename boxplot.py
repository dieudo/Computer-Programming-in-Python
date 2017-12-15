# boxplot.py
import matplotlib.pyplot as plt
import numpy as np

# Random test data
data1 = np.random.normal(0, 1, 20)
data2 = np.random.normal(2, 2, 20)
data = [data1, data2]

plt.figure(figsize=(5, 4))
plt.boxplot(data)

plt.show()
