# Ejercicio 1 – Serie de Fibonacci
# Se genera la serie de Fibonacci hasta n términos solicitados por el usuario.
# Cada término se obtiene sumando los dos anteriores, partiendo desde 0 y 1.

# 1. Solicitar la cantidad de términos a generar
n = int(input("Ingrese la cantidad de términos n: "))

# 2. Inicializar la serie con los dos primeros términos base
serie_fibo = [0, 1]

# 3. Acumular los siguientes términos: F(i) = F(i-1) + F(i-2)
for i in range(2, n):
    siguiente_termino = serie_fibo[-1] + serie_fibo[-2]
    serie_fibo.append(siguiente_termino)

# 4. Mostrar los primeros n términos (slicing maneja casos n < 2)
print(f"Serie de Fibonacci ({n} términos): {serie_fibo[:n]}")