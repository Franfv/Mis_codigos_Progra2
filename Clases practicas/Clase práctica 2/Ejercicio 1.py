#Ejercicio 1:
# |hay que hacer 3 funciones segun lo que piden:

#datos de los voltajes:

voltajes = [12.6 , 12.4 , 12.3 , 12.1 , 11.9 , 11.8 , 11.6 , 11.4]

import random
#lista:
voltajes = [round(random.uniform(10.0,12.0),1) for _ in range(10)]

def analizar_voltajes(lista_voltajes):
    #la funcion debe calcular:
    #• Voltaje máximo
    #• Voltaje mínimo
    #• Voltaje promedio
    #• Cantidad de mediciones bajo 12.0 V

    maximo_V = max(lista_voltajes)
    minimo_V = min(lista_voltajes)

    #Voltaje promedio:
    promedio_V = sum(lista_voltajes) / len(lista_voltajes)
    return maximo_V, minimo_V, promedio_V

#hay que llamar la funcion, de nada sirve que esté definida:
analizar_voltajes(promedio_V)
print(f'El promedio es: {promedio_V}')
