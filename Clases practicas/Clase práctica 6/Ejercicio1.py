#Ejercicio 1 – Instrumentación Electrónica – El Laboratorio de Medición

# a) Clase base Instrumento
class Instrumento:
    # Atributo de clase compartido por todos los instrumentos
    unidad_estandar = 'SI'
    
    def __init__(self, marca, modelo):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo

    # b) Método estático para convertir milis a unidad base
    @staticmethod
    def convertir_a_base(valor_mili):
        # Convierte milis a unidad base (ej: 500 mV -> 0.5 V)
        return valor_mili / 1000


# c) Clase heredera Osciloscopio
class Osciloscopio(Instrumento):
    def __init__(self, marca, modelo, v_div=1.0):
        # Heredamos marca y modelo desde la clase padre
        super().__init__(marca, modelo)
        # Atributo propio
        self.v_div = v_div

    # d) Método para actualizar v_div
    def actualizar_vdiv(self, nuevo_vdiv):
        self.v_div = nuevo_vdiv
    
    # Método para mostrar configuración
    def mostrar_configuracion(self):
        print(f"Osciloscopio {self.marca} {self.modelo}")
        print(f"Voltaje por división: {self.v_div} V/div")
        print(f"Unidad estándar: {Instrumento.unidad_estandar}")


# e) Instanciación y convierta 500mV a su base usando el método 
# estático e imprima el resultado.

osciloscopio1 = Osciloscopio("Tektronix", "TDS2024C")

# Convertimos 500 mV a V
resultado = Instrumento.convertir_a_base(500)
print("500 mV en base:", resultado, "V") 

# Mostramos configuración del osciloscopio
osciloscopio1.mostrar_configuracion()
