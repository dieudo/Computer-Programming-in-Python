# axes2.py
import numpy as np
import matplotlib.pyplot as plt

ax1 = plt.axes([0.1, 0.1, 0.5, 0.5])
ax2 = plt.axes([0.2, 0.2, 0.5, 0.5])
ax3 = plt.axes([0.3, 0.3, 0.5, 0.5])
ax4 = plt.axes([0.4, 0.4, 0.5, 0.5])

plt.savefig("axes2.png", dpi=72)
plt.show()
