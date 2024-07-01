import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros del sistema (puedes ajustarlos)
σ = 10.0  # sigma
ρ = 30.0  # rho
β = 8.0 / 3.0  # beta

# Condiciones iniciales (puedes cambiarlas)
x0, y0, z0 = (1.0, 1.0, 1.0)

# Función que define el sistema de ecuaciones diferenciales
def lorenz(state, t, a, b, c):
    x, y, z = state
    dxdt = a * (y - x)
    dydt = x * (b - z) - y
    dzdt = x * y - c * z
    return dxdt, dydt, dzdt

# Tiempo de integración
t = np.linspace(0, 25, 10000)  # Ajusta el rango y la cantidad de puntos si es necesario

# Resolver el sistema de ecuaciones
sol = odeint(lorenz, (x0, y0, z0), t, args=(σ, ρ, β))

# Extraer las coordenadas x, y, z
x, y, z = sol.T

# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el atractor de Lorenz
ax.plot(x, y, z, lw=0.5)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Atractor de Lorenz")

# Mostrar la gráfica
plt.show()
