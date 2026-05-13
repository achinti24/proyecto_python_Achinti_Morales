# datos.py - Maneja la lectura y escritura del archivo JSON.
# Todos los demas modulos usan guardar_datos() para guardar cambios.
 
import json
import os
 
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
 
# Recibe la lista de gastos y la guarda en el archivo JSON.
def guardar_datos(gastos):
    archivo = open(ARCHIVO, "w")
    json.dump(gastos, archivo)
    archivo.close()
 