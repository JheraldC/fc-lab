import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from magpylib.source.magnet import Cylinder

# Crear una fuente magnética: un cilindro magnetizado
cylinder = Cylinder(mag=(0, 0, 1000), dim=(3, 5))

# Crear la figura y los ejes
fig = plt.figure(figsize=(12, 6))

# Eje 3D
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_xlim([-10, 10])
ax1.set_ylim([-10, 10])
ax1.set_zlim([-10, 10])

# Eje 2D
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

# Calcular el campo magnético en cada punto de la malla
positions = np.stack((X, Y, Z), axis=-1).reshape(-1, 3)
B = cylinder.getB(positions).reshape(100, 100, 3)

# Separar las componentes del campo magnético
Bx = B[:, :, 0]
Bz = B[:, :, 2]

# Graficar el cilindro en 3D
theta = np.linspace(0, 2 * np.pi, 100)
x_cyl = 1.5 * np.cos(theta)
z_cyl = 1.5 * np.sin(theta)
y_cyl = np.linspace(-2.5, 2.5, 100)

Xc, Zc = np.meshgrid(x_cyl, y_cyl)
Yc = np.zeros_like(Xc)

ax1.plot_surface(Xc, Zc, Yc, alpha=0.3, rstride=20, cstride=10)
# Graficar el campo magnético en el plano XZ
ax2.streamplot(X, Z, Bx, Bz, color='b', linewidth=1)

plt.tight_layout()
plt.show()
