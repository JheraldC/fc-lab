def main():
    masa1 = float(input("Escriba la masa del objeto 1 (kg): "))
    masa2 = float(input("Escriba la masa del objeto 2 (kg): "))
    if (masa1 > masa2):
        aceleracion = calcular_aceleracion(masa1, masa2)
        tension = AtwoodMachine(masa1, masa2)
        print("Los objetos con sus masas ingresadas tiene una aceleracion de", aceleracion, "m/s^2 y una tension de", tension, "N")
    else:
        print("Las masas ingresadas no son válidas (m1 > m2).")

def AtwoodMachine(masa1, masa2):
    #Calcular tension
    gravedad = 9.81
    aceleracion = calcular_aceleracion(masa1, masa2)
    tension = masa1 * gravedad - masa1 * aceleracion 
    return tension

def calcular_aceleracion(masa1, masa2):
    #Calcular aceleracion
    gravity = 9.81
    numerador = (masa1 - masa2) * gravity
    denominador = masa1 + masa2 
    aceleracion = numerador / denominador
    return aceleracion

main()
