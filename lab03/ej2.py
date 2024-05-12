import numpy as np
import matplotlib.pyplot as plt

# Función para calcular el campo eléctrico
def E(q, r0, x, y):
    den = np.hypot(x - r0[0], y - r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

# Configuración de la red de puntos
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

# Ingresar las cargas
charges = []
num_charges = int(input("Ingrese el número de cargas: "))
for i in range(num_charges):
    q = float(input(f"Ingrese la carga {i + 1}: "))
    charges.append(q)

# Crear un campo eléctrico
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
positions = np.linspace(-1.5, 1.5, num_charges)  # Distribución de posiciones en el rango [-1.5, 1.5]
for i, charge in enumerate(charges):
    ex, ey = E(charge, (positions[i], 0), x=X, y=Y)
    Ex += ex
    Ey += ey

# Graficar el campo eléctrico
plt.streamplot(x, y, Ex, Ey, color='b')
plt.scatter(positions, np.zeros(num_charges), c='r', s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
