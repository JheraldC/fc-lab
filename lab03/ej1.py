import matplotlib.pyplot as plt

def main():
    form = input("Desea usar la formula de Fuerza Electrica(F) o Intensidad de campo(E)?:")
 
    N = 30  # Límite del array
    distancias = []
    for i in range(1, N + 1, 1):
        distancias.append(i)

    if form == 'F':
        q1 = float(input("Ingrese el valor de la primera carga: "))
        q2 = float(input("Ingrese el valor de la segunda carga: "))
        showGraphic(q1, q2, distancias)
    elif form == 'E':
        q1 = float(input("Ingrese el valor de la carga: "))
        showGraphic(q1, distancias)
    else:
        print("Parametros no válidos.")

def fuerzaElectrica(q1, q2, r):
    k = 9 * (10**9)  # Constante de Coulomb
    return (k * q1 * q2) / (r**2)

def intensidadCampo(q1, r):
    k = 9 * (10**9)  # Constante de Coulomb
    return (k * q1) / (r**2)

def showGraphic(*args):
    resultados = []
    if len(args) == 2:
        for r in args[1]:
            resultado = intensidadCampo(args[0], r)
            resultados.append(resultado)
        plt.plot(args[1], resultados)
        plt.xlabel("Distancia (m^2)")
        plt.ylabel("Intensidad de Campo (N/C)")
        plt.title("Intensidad de Campo en función de la Distancia")
        plt.grid(True)
        plt.show()
    elif len(args) == 3:
        for r in args[2]:
            resultado = fuerzaElectrica(args[0], args[1], r)
            resultados.append(resultado)
        plt.plot(args[2], resultados)
        plt.xlabel("Distancia (m^2)")
        plt.ylabel("Fuerza Eléctrica (N)")
        plt.title("Fuerza Eléctrica en función de la Distancia")
        plt.grid(True)
        plt.show()

main()

