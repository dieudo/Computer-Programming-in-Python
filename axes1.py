# axes1.py
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

ax1 = plt.axes([0.1, 0.1, 0.8, 0.8])
plt.plot(X,S)
ax2 = plt.axes([0.2, 0.6, 0.3, 0.3])
plt.plot(X,C)

plt.savefig("axes1.png", dpi=72)
plt.show()
