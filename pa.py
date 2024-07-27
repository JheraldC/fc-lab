
import numpy as np

# Datos del problema
epsilon0 = 8.854e-12
q = 1e-9
R = 0.1  # Radio de la esfera
N = 1000

# Discretización de la esfera
theta = np.linspace(0, np.pi, N)
phi = np.linspace(0, 2 * np.pi, N)
theta, phi = np.meshgrid(theta, phi)
x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)

# Cálculo del campo eléctrico
r = np.sqrt(x**2 + y**2 + z**2)
E = np.zeros_like(r)
E[r > R] = (1 / (4 * np.pi * epsilon0)) * q / r[r > R]**2  # Campo fuera de la esfera

# Cálculo del flujo eléctrico
dS = R**2 * np.sin(theta) * (np.pi / N)**2
flujo_electrico = np.sum(E * dS)

# Verificación de la ley de Gauss
if np.isclose(flujo_electrico, q / epsilon0, rtol=1e-3):
    print("La ley de Gauss se cumple dentro de la tolerancia.")
else:
    print("La ley de Gauss no se cumple dentro de la tolerancia.")

