import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 1000)  # Limited range for better visualization
s = x**3
c = np.sin(x)
d = np.exp(x)
l = np.log(x + 1)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, s, label=r'$ f(x) = x^3 $', c='g', linestyle='-.', marker='*', markersize=5)
plt.title(r"$ f(x) = x^3 $")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, c, label=r'$ f(x) = \sin(x) $', c='crimson', linestyle=':', marker='o', markersize=5)
plt.title(r"$ f(x) = \sin(x) $")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, d, label=r'$ f(x) = e^x $', c='b', linestyle='-.', marker='.', markersize=5)
plt.title(r"$ f(x) = e^x $")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, l, label=r'$ f(x) = \log(x+1) $', c='purple', linestyle=':', marker='+', markersize=5)
plt.title(r"$ f(x) = \log(x+1) $ (for $ x \geq 0 $)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.tight_layout()
plt.show()
