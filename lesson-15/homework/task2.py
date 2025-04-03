import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2/np.pi, 10000)

s = np.sin(x)
c = np.cos(x)


plt.plot( x, s,  label='$sin(x) $', c='g', linestyle='-.', marker='*', markersize=5)
plt.plot(x,c, label='$ cos(x) $ ', c='crimson', linestyle=':', marker='o', markersize=5)
plt.title('Plot of the function $ sin(x) $ and $ cos(x) $')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()