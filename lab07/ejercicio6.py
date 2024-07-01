import numpy as np

# Parámetros
N = 100000

# Función original
def f(x):
    return np.e**(-x) 

# Transformación de variable y función ajustada
def transformed_f(u):
    x = (1 - u) / u
    return f(x) * (1 / u**2)

# Método de Monte Carlo
def monte_carlo(f, n):
    u = np.random.uniform(0, 1, n)
    fx = f(u)
    integral = np.mean(fx)
    return integral

# Calcular la integral
res = monte_carlo(transformed_f, N)

valueTeo = 1.0

# Cálculo del error relativo y error teórico
relative_error = abs((res - valueTeo) / valueTeo)
error_teorico = 1 / np.sqrt(N)

print(f'Valor Monte Carlo: {res:.8f}')
print(f'Valor Teórico: {valueTeo:.8f}')
print(f'Error Relativo: {relative_error:.8f}')
print(f'Error Teórico: {error_teorico:.8f}')

