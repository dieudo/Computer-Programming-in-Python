# animation3d.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111,projection='3d')
ax.set_zlim(-1, 1)
xs =ys= np.linspace(-1, 1, 30)
X, Y = np.meshgrid(xs, ys)
wframe = None
for phi in np.arange(360):  #360 degrees
    if wframe != None: # Remove old lines before drawing
        ax.collections.remove(wframe)
    Z = np.cos(2 * np.pi * X + phi) * \
        (1 - np.sqrt(X**2 + Y**2))
    wframe = ax.plot_wireframe(X, Y, Z)
    ax.view_init(azim=phi, elev=50)
    plt.pause(0.05)
