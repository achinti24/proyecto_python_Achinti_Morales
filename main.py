# main.py - Archivo principal del Simulador de Gasto Diario.
# Muestra el menu y llama a las funciones de cada modulo segun lo que elija el usuario.
# Tambien se encarga de cargar y guardar los datos en el archivo JSON.

import json
import os
from registrar import registrar_gasto
from listar import listar_gastos
from calcular import calcular_totales
from reporte import generar_reporte

ARCHIVO = "gastos.json"

# Lee el archivo JSON y retorna la lista de gastos.
# Si el archivo no existe o esta vacio, retorna una lista vacia.
def cargar_datos():
    if os.path.exists(ARCHIVO):
        archivo = open(ARCHIVO, "r")
        contenido = archivo.read()
        archivo.close()
        if contenido == "":
            return []
        return json.loads(contenido)
    else:
        return []

# Recibe la lista de gastos y la escribe en el archivo JSON.
def guardar_datos(gastos):
    archivo = open(ARCHIVO, "w")
    json.dump(gastos, archivo)
    archivo.close()

print("Bienvenido al Simulador de Gasto Diario")
print("Cargando datos...")

gastos = cargar_datos()

print("Gastos cargados: " + str(len(gastos)))

salir = False

while salir == False:
    print("")
    print("========================================")
    print("      SIMULADOR DE GASTO DIARIO")
    print("========================================")
    print("1. Registrar gasto")
    print("2. Listar gastos")
    print("3. Calcular totales")
    print("4. Generar reporte")
    print("5. Salir")
    print("========================================")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        gastos = registrar_gasto(gastos, guardar_datos)

    elif opcion == "2":
        listar_gastos(gastos)

    elif opcion == "3":
        calcular_totales(gastos)

    elif opcion == "4":
        generar_reporte(gastos)

    elif opcion == "5":
        print("Hasta luego!")
        salir = True

    else:
        print("Opcion no valida. Elige entre 1 y 5.")