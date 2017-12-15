# barh.py
import numpy as np
import matplotlib.pyplot as plt

cities = ('NY', 'LA', 'Chicago')
y_pos = np.arange(len(cities))
wind = [10, 5, 13]
error = [3, 1, 2]
plt.barh(y_pos, wind, xerr=error, \
         align='center', alpha=0.4)
plt.yticks(y_pos, cities)
plt.xlabel('Wind Speed')
plt.title('Average wind speed at three cities')
plt.show()
