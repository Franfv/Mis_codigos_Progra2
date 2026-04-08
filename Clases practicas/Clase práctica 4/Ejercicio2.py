import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 2 – Calidad del Aire – Estadísticas y Resumen

# a) Cargue el archivo y verifique la estructura del dataset (dimensiones y tipos de datos) 
# usando las propiedades shape y dtypes.
df = pd.read_csv('calidad_aire.csv')

# Verificar dimensiones
print("Dimensiones:", df.shape)
# Verificar tipos de datos
print('Tipos de datos:\n', df.dtypes) #agrega un salto de linea

# b) Utilice el método .describe() para obtener un resumen estadístico de todas las 
# variables y determine visualmente cuál es el valor máximo de co2 registrado.
print('\nResumen estadistico: ')
print(df.describe()) # -> esto nos dará el max media y min. LEER CW

# | Segun el CW, el max de co2 es de: 553.9 |
#con codigo es:
max_co2 = df['co2'].max()
print('\nEl valor maximo de co2 registrado es: ', max_co2)

# c) 