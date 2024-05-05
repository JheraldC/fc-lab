import matplotlib.pyplot as plt

def main():
    masa = float(input("Escribe la masa del objeto (kg): "))
    distancia = float(input("Escribe la distancia recorrida (m): "))
    tiempo = float(input("Escribe el tiempo transcurrido (s): "))
    velocidad_inicial = float(input("Escribe la velocidad inicial (m/s): "))
    velocidad_final = float(input("Escribe la velocidad final (m/s): "))
    fuerza = calcular_fuerza(masa, distancia, tiempo, velocidad_inicial, velocidad_final)
    print("La fuerza que describe el móvil es:", fuerza, "N")

    # Graficar el proceso de cambio de velocidad
    tiempo_total = tiempo + 1
    tiempos = list(range(int(tiempo_total)))
    velocidades = [velocidad_inicial + (velocidad_final - velocidad_inicial) * (t / tiempo) for t in tiempos]

    plt.plot(tiempos, velocidades)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Cambio de velocidad del móvil')
    plt.grid(True)
    plt.show()


def calcular_fuerza(masa, distancia, tiempo, velocidad_inicial, velocidad_final):
    aceleracion = (velocidad_final - velocidad_inicial) / tiempo
    fuerza = masa * aceleracion
    return fuerza

main()
