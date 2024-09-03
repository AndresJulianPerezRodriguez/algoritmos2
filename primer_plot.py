import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,2*np.pi,400)
a = 7
b = 5
x = np.cos(a*t)
y = np.sin(b*t)
plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
