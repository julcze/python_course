import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_knots = np.linspace(-2*np.pi,2*np.pi,201)
y_knots = np.linspace(-2*np.pi,2*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
Z = X**2-Y**2
ax = Axes3D(plt.figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()
