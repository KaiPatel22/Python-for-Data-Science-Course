import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 5.0, 0.1)
y = np.cos(2 * np.pi * x) * np.exp(-x)
plt.plot(x, y, label='Graph')