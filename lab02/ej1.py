def main():
    masa1 = float(input("Escriba la masa del objeto 1 (kg): "))
    masa2 = float(input("Escriba la masa del objeto 2 (kg): "))
    tension = AtwoodMachine(masa1, masa2)
    print("Los objetos con sus masas ingresadas tiene una tension ")

def AtwoodMachine(masa1, masa2):
    #Calcular aceleracion
    gravity = 9.81
    numerador = (masa1 - masa2) * gravity
    denominador = masa1 + masa2 
    aceleracion = numerador / denominador
    #Calcular tension
    tension = masa1 * gravity - masa1 * aceleracion 
    return tension

def calcular_aceleracion(masa1, masa2):
