def main():
    metodo = input("¿La ecuación será MRU o MRUV?: ").upper()
    
    match metodo:
        case "MRU":
            variable = input("¿Escriba la variable que desea calcular?(d, t, v): ").lower()
            match variable:
                case "d":
                    v = float(input("Escriba la velocidad (m/s): "))
                    t = float(input("Escriba el tiempo (s): "))
                    print("La distancia es", v * t, "metros")
                case "v":
                    d = float(input("Escriba la distancia (m): "))
                    t = float(input("Escriba el tiempo (s): "))
                    print("La velocidad es", d / t, "m/s")
                case "t":
                    d = float(input("Escriba la distancia (m): "))
                    v = float(input("Escriba la velocidad (m/s): "))
                    print("El tiempo es", d / v, "s")
                case other:
                    print("Variable no válida")
        case "MRUV":
            variable = input("¿Escriba la variable que desea calcular?(d, a, t, Vo, Vf): ").lower()
            match variable:
                case "d":
                    Vo = float(input("Escriba la velocidad inicial (m/s): "))
                    t = float(input("Escriba el tiempo (s): "))
                    a = float(input("Escriba la aceleración (m/s^2): "))
                    print("La distancia es", Vo * t + 0.5 * a * t ** 2, "metros")
                case "a":
                    Vf = float(input("Escriba la velocidad final (m/s): "))
                    Vo = float(input("Escriba la velocidad inicial (m/s): "))
                    t = float(input("Escriba el tiempo (s): "))
                    print("La aceleración es", ((Vf - Vo) / t), "m/s^2")
                case "t":
                    Vf = float(input("Escriba la velocidad final (m/s): "))
                    Vo = float(input("Escriba la velocidad inicial (m/s): "))
                    a = float(input("Escriba la aceleración (m/s^2): "))
                    print("El tiempo es", ((Vf - Vo) / a) ** 0.5, "s")
                case "vo":
                    Vf = float(input("Escriba la velocidad final (m/s): "))
                    a = float(input("Escriba la aceleración (m/s^2): "))
                    t = float(input("Escriba el tiempo (s): "))
                    print("La velocidad inicial es", Vf - a * t, "m/s")
                case "vf":
                    Vo = float(input("Escriba la velocidad inicial (m/s): "))
                    a = float(input("Escriba la aceleración (m/s^2): "))
                    t = float(input("Escriba el tiempo (s): "))
                    print("La velocidad final es", Vo + a * t, "m/s")
                case other:
                    print("Variable no válida")
        case other:
            print("Método no válido")
main()
