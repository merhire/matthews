import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num_points = 100
x_line = np.linspace(-5, 5, num_points)
y_line = np.linspace(-5, 5, num_points)

X, Y = np.meshgrid(x_line, y_line)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(
    X, Y, Z,
    cmap='viridis',
    linewidth=0,
    antialiased=True
)

ax.set_title(r'График поверхности $z = \sin(\sqrt{x^2 + y^2})$', fontsize=16)
ax.set_xlabel('Ось X', fontsize=12)
ax.set_ylabel('Ось Y', fontsize=12)
ax.set_zlabel('Ось Z', fontsize=12)

fig.colorbar(surface, shrink=0.5, aspect=5, label='Значение Z')

ax.view_init(elev=30, azim=45)
plt.savefig('lab4_5.png', dpi=1000)
plt.show()