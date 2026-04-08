# --- Datos para el Ejercicio 1 (Diccionarios) ---
red_esp8266 = {
    "Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000},
    "Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0},
    "Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150},
    "Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000},
}


def auditar_red(nodos):
    for nombre, datos in nodos.items(): 
        #la cantidad total de nodos registrados.
        print(f"Cantidad total de nodos registrados: {len(nodos)}")

#lista con las direcciones IP de los nodos que están en estado "falla" o ïnactivo" 
        
        if datos["estado"] in ["falla", "inactivo"]:
            print(f"REVISAR FALLA: {datos[nombre]} - IP: {datos['ip']}")

#El valor promedio de la "salida_dac", considerando solo los nodos en estado.activo".
        if datos["estado"] == "activo":
            salida_dac = sum(datos)/len(datos)
    print(f"Valor promedio de salida_dac para nodos activos: {salida_dac}")


            