import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del modelo
alpha = 2/3  # Tasa de crecimiento de presas
beta = 4/3  # Tasa de depredación
gamma = 1.0  # Tasa de mortalidad de depredadores
delta = 1.0  # Tasa de reproducción de depredadores por presa

# Función para el sistema de ecuaciones diferenciales
def modelo(y, t):
    x, y = y  # x: presas, y: depredadores
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return dxdt, dydt

# Condiciones iniciales
x0 = 10.0  # Población inicial de presas
y0 = 5.0   # Población inicial de depredadores

# Simulación
t = np.linspace(0, 15, 1000)
solucion = odeint(modelo, [x0, y0], t)

# Sección de Poincaré (plano x = x0)
puntos_seccion = [(x, y) for x, y in solucion if abs(x - x0) < 0.1]

# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(solucion[:, 0], solucion[:, 1], label="Trayectoria")
plt.scatter(*zip(*puntos_seccion), c='red', s=5, label="Sección de Poincaré")
plt.xlabel("Presas (x)")
plt.ylabel("Depredadores (y)")
plt.title("Sección de Poincaré para el modelo depredador-presa")
plt.legend()
plt.grid(True)
plt.show()

