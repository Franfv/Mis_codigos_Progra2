import numpy as np
import matplotlib.pyplot as plt

# En este ejercicio, se utilizara arreglos paramétricos para dibujar la serie de Fibonacci:

# 1. solicitar coeficientes 'n' al usuario para construir la espiral:
n = int(input('Ingrese los coeficientes n que desea utilizar para construir la espiral (entre 6-12): '))

# 2. Genere una lista con los primeros n términos de la serie de Fibonacci:
serie_fibo = [0,1] #dos primeros valores manuales para empezar.

# Como ya tenemos 2 términos, iteramos desde el tercer término hasta n
for i in range(2, n):
    # Sumamos el último [-1] y el penúltimo [-2] término de la lista
    siguiente_termino = serie_fibo[-1] + serie_fibo[-2]
    # Lo agregamos a nuestra serie
    serie_fibo.append(siguiente_termino)

# (Opcional) Puedes imprimirla para verificar que se generó bien
print(f"Serie generada: {serie_fibo}")

# 3. Utilice funciones trigonométricas:
radio = np.linspace(0,2*np.pi,100)