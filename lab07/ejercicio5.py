import numpy as np

# Parámetros y valor teórico
valueTeo = 2.7645 
a, b = 0, 1
N = 100000
print('Integral:')

def monte_carlo(f, a, b, n):
    x = np.random.uniform(a, b, n)
    fx = f(x)
    integral = (b - a) * np.mean(fx)
    return integral

def f(x):
    return (np.e)**(x+x**2)

res = monte_carlo(f, a, b, N)

relative_error = abs((res - valueTeo) / valueTeo)

error_teorico = 1 / np.sqrt(N)

print(f'Valor Monte Carlo: {res:.8f}')
print(f'Valor Teórico: {valueTeo:.8f}')
print(f'Error Relativo: {relative_error:.8f}')
print(f'Error Teórico: {error_teorico:.8f}')

