import numpy as np
import matplotlib.pyplot as plt

regla = {
    (1, 1, 1): 0,
    (1, 1, 0): 0,
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0,
}

def automata_celular(regla, num_celdas, num_generaciones, condicion_borde="periodica"):
    """Simula un autómata celular elemental."""
    estado_actual = np.random.randint(2, size=num_celdas)
    historial = np.zeros((num_generaciones, num_celdas), dtype=np.int8)
    historial[0] = estado_actual

    for gen in range(1, num_generaciones):
        nuevo_estado = np.zeros(num_celdas, dtype=np.int8)
        for i in range(num_celdas):
            izquierda = (i - 1) % num_celdas if condicion_borde == "periodica" else max(0, i - 1)
            centro = i
            derecha = (i + 1) % num_celdas if condicion_borde == "periodica" else min(num_celdas - 1, i + 1)

            nuevo_estado[i] = regla[(estado_actual[izquierda], estado_actual[centro], estado_actual[derecha])]

        estado_actual = nuevo_estado
        historial[gen] = nuevo_estado

    return historial

# Parámetros de simulación
num_celdas = 50
num_generaciones = 20
condicion_borde = "periodica"

# Ejecutar la simulación
historial = automata_celular(regla, num_celdas, num_generaciones, condicion_borde)

# Visualizar el resultado
plt.figure(figsize=(10, 8))  # Ajustamos el tamaño para que sea más ancho y menos alto
plt.imshow(historial, cmap='binary', interpolation='nearest', aspect='auto')
plt.title("Autómata Celular - Regla 30")  # El título ya no necesita ser dinámico
plt.xlabel("Celda")
plt.ylabel("Generación")
plt.xticks(np.arange(0, num_celdas, 10))
plt.yticks(np.arange(0, num_generaciones, 10))
plt.show()

