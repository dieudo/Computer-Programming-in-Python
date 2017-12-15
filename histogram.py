# histogram.py
import numpy as np
import matplotlib.pyplot as plt

mu = 100  # mean of distribution
sigma = 15  # std
x = mu + sigma * np.random.randn(10000)
num_bins = 30
plt.figure(figsize=(5, 4))
n, bins, patches = plt.hist(x, num_bins,
    facecolor='green', edgecolor='k', alpha=0.5)
plt.xlabel('Value of x')
plt.ylabel('Count')
plt.title(r'$\mu=100$, $\sigma=15$')
plt.show()
