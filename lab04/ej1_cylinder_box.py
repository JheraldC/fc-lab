import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import magpylib as magpy
from magpylib.source.magnet import Cylinder, Box

# Crear las fuentes magnéticas
cylinder = Cylinder(mag=(0, 0, 1000), dim=(3, 5))
box = Box(mag=(0, 0, 500), dim=(4, 4, 4), pos=(6, 0, 0))

# Crear la figura y los ejes
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.set_xlim([-10, 10])
ax1.set_ylim([-10, 10])
ax1.set_zlim([-10, 10])

ax2 = fig.add_subplot(122)
ax2.set_xlim([-10, 10])
ax2.set_ylim([-10, 10])
ax2.set_xlabel('X [mm]')
ax2.set_ylabel('Z [mm]')
ax2.set_title('Campo Magnético en el Plano XZ')

# Definir una malla de puntos en el plano XZ
x = np.linspace(-10, 10, 100)
z = np.linspace(-10, 10, 100)
X, Z = np.meshgrid(x, z)
Y = np.zeros_like(X)  # Plano Y=0

# Calcular el campo magnético de ambas fuentes
positions = np.stack((X, Y, Z), axis=-1).reshape(-1, 3)
B_cylinder = cylinder.getB(positions)
B_box = box.getB(positions)
B_total = B_cylinder + B_box
B_total = B_total.reshape(100, 100, 3)

# Separar las componentes del campo magnético
Bx = B_total[:, :, 0]
Bz = B_total[:, :, 2]

# Graficar el cilindro en 3D
theta = np.linspace(0, 2 * np.pi, 100)
x_cyl = 1.5 * np.cos(theta)
z_cyl = 1.5 * np.sin(theta)
y_cyl = np.linspace(-2.5, 2.5, 100)

Xc, Zc = np.meshgrid(x_cyl, y_cyl)
Yc = np.zeros_like(Xc)

ax1.plot_surface(Xc, Zc, Yc, alpha=0.3, rstride=20, cstride=10, color='r')

# Graficar la caja en 3D
x_box = np.linspace(4, 8, 10)
y_box = np.linspace(-2, 2, 10)
z_box = np.linspace(-2, 2, 10)

Xb, Zb = np.meshgrid(x_box, z_box)
Yb1, Yb2 = np.meshgrid(y_box, y_box)

# Superficies de la caja
ax1.plot_surface(Xb, Zb, np.full_like(Xb, 2), alpha=0.3, color='b')
ax1.plot_surface(Xb, Zb, np.full_like(Xb, -2), alpha=0.3, color='b')
ax1.plot_surface(np.full_like(Yb1, 4), Yb1, Yb2, alpha=0.3, color='b')
ax1.plot_surface(np.full_like(Yb1, 8), Yb1, Yb2, alpha=0.3, color='b')
ax1.plot_surface(Yb1, np.full_like(Yb1, -2), Yb2, alpha=0.3, color='b')
ax1.plot_surface(Yb1, np.full_like(Yb1, 2), Yb2, alpha=0.3, color='b')

# Graficar el campo magnético en el plano XZ
ax2.streamplot(X, Z, Bx, Bz, color='b', linewidth=1)

plt.tight_layout()
plt.show()
