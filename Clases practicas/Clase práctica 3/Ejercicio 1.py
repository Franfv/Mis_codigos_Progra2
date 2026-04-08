#Ejercicio 1 – Análisis de Señales de Sensores en un Brazo Robótico - ppt clase 4 numpy - 
import numpy as np
import matplotlib.pyplot as plt

#array de tiempo:
t = np.linspace(0,10,500)
 
#matriz de NumPy de posiciones de tamaño 3 × 500. 
matriz = np.zeros((3,500)) #3 filas (x,y,z) con 500 columnas

"""
posiciones[0, :] → toda la fila 0 (coordenada x) - 1era fila
posiciones[1, :] → toda la fila 1 (coordenada y) - 2da fila
posiciones[2, :] → toda la fila 2 (coordenada z) - 3era fila
"""

matriz[0,:] = 2*np.sin(t) #x(t)
matriz[1,:] = 2*np.cos(t) #y(t)
matriz[2,:] = 0.5*t

# Utilizando la manipulación de matrices (slicing), extrae cada fila en variables independientes (x, y, z):
# Es decir extraer fila:
x = matriz[0,:]
y = matriz[1,:]
z = matriz[2,:]


