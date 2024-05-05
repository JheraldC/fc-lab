import matplotlib.pyplot as plt

def main():
    masa = float(input("Escribe la masa del objeto (kg): "))
    distancia = float(input("Escribe la distancia recorrida (m): "))
    tiempo = float(input("Escribe el tiempo transcurrido (s): "))
    velocidad_inicial = float(input("Escribe la velocidad inicial (m/s): "))
    velocidad_final = float(input("Escribe la velocidad final (m/s): "))
    fuerza = calcular_fuerza(masa, distancia, tiempo, velocidad_inicial, velocidad_final)


def calcular_fuerza(masa, distancia, tiempo, velocidad_inicial, velocidad_final):
    aceleracion = (velocidad_final - velocidad_inicial) / tiempo
    fuerza = masa * aceleracion
    return fuerza
