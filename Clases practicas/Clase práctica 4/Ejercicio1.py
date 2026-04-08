import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Ejercicio 1 – Sensor Ambiental – Limpieza y Transformación

# a) Cargue el archivo y utilice el método dropna() para eliminar cualquier fila que contenga valores nulos.

df = pd.read_csv('sensor_datos.csv')
df = df.dropna() #Elimina filas con nulos

# b) Generar nueva columna "Potencia_W" realizando la operación vectorizada P = V · I:
df['Potencia_W'] =df['voltaje'] * df['corriente'] 

# c) Cree una columna booleana llamada "Alerta_Humedad" que identifique con 
# True aquellos registros donde la humedad sea superior al 70 % 
df['Alerta_Humedad'] = df['humedad'] > 70

# d) Utilizando matplotlib, grafique en un mismo lienzo la Temperatura y la Potencia_W]
plt.figure(figsize=(10,5))
plt.plot(df['fecha'], df['temperatura'], label='Temperatura (°C)', color='blue')
plt.plot(df['fecha'], df['Potencia_W'], label='Potencia (W)', color='red')

# e) Mejore la visualización activando la grilla con plt.grid(True) y rotando las etiquetas del eje X
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=90) # para rotar a 45°
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.legend() # para mostrar la leyenda de las líneas
plt.title('Temperatura (°C) Vs Potencia (W)')
plt.show()


