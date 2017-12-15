# barv.py
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(8)
Y = np.sin(X)
plt.figure(figsize=(5, 4))
plt.bar(X, Y)
for i in X:
    if Y[i] >= 0:
        plt.text(X[i], Y[i] + 0.05, '{0:0.2f}'.format(Y[i]))
    else:
        plt.text(X[i], Y[i] - 0.10, '{0:0.2f}'.format(Y[i]))

plt.ylim(-1.1, 1.1)
plt.xticks(())
plt.yticks(())
plt.show()
