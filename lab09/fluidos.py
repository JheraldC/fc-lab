import numpy as np
import matplotlib.pyplot as plt

# Parámetros del flujo
Re = 100  # Número de Reynolds
dt = 0.01  # Paso de tiempo

# Condiciones iniciales (posición de una partícula de fluido)
x0 = 1.0
y0 = 0.0

# Función para calcular la velocidad del fluido (ejemplo simplificado)
def velocidad_fluido(x, y):
    vx = 1 - (y**2) / (x**2 + y**2)**2
    vy = -2 * x * y / (x**2 + y**2)**2
    return vx, vy

# Simulación
posiciones = [(x0, y0)]
for _ in range(1000):
    x, y = posiciones[-1]
    vx, vy = velocidad_fluido(x, y)
    x += vx * dt
    y += vy * dt
    posiciones.append((x, y))

# Sección de Poincaré
seccion_x = 1.5  # Posición x de la sección de Poincaré
puntos_seccion = [(x, y) for x, y in posiciones if abs(x - seccion_x) < 0.01]

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(*zip(*posiciones), s=1, label="Trayectoria")
plt.scatter(*zip(*puntos_seccion), c='red', s=5, label="Sección de Poincaré")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sección de Poincaré para flujo alrededor de un cilindro (Re = 100)")
plt.legend()
plt.grid(True)
plt.show()

