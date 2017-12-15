# gridspec1.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)

gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
plt.plot(X,C)
ax2 = plt.subplot(gs[1,:-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])

plt.savefig("gridspec1.png", dpi=72)
plt.show()
