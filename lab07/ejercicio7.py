import numpy as np

valueTeo = 0.589048
a, b = 0, 1
N = 100000

# Función a integrar
def f(x):
    return (1 - x**2)**(3/2)

# Método de Monte Carlo
def monte_carlo(f, a, b, n):
    x = np.random.uniform(a, b, n)
    fx = f(x)
    integral = (b - a) * np.mean(fx)
    return integral

res = monte_carlo(f, a, b, N)

# Cálculo del error relativo y error teórico
relative_error = abs((res - valueTeo) / valueTeo)
error_teorico = 1 / np.sqrt(N)

print(f'Valor Monte Carlo: {res:.8f}')
print(f'Valor Teórico: {valueTeo:.8f}')
print(f'Error Relativo: {relative_error:.8f}')
print(f'Error Teórico: {error_teorico:.8f}')

