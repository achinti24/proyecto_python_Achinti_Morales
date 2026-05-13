# registrar.py - Permite al usuario ingresar un nuevo gasto.
# Pide cantidad, categoria y descripcion, luego lo guarda en el archivo JSON.
 
import datetime
from datos import guardar_datos
 
def registrar_gasto(gastos):
    print("")
    print("===== REGISTRAR GASTO =====")
 
    # Pedir la cantidad
    cantidad = 0
    while cantidad <= 0:
        texto = input("Cantidad del gasto: $")
        try:
            cantidad = float(texto)
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
        except:
            print("Ingresa un numero valido.")
            cantidad = 0
 
    # Pedir la categoria
    print("")
    print("Categorias:")
    print("1. Comida")
    print("2. Transporte")
    print("3. Entretenimiento")
    print("4. Salud")
    print("5. Educacion")
    print("6. Ropa")
    print("7. Otros")
 
    categorias = ["comida", "transporte", "entretenimiento", "salud", "educacion", "ropa", "otros"]
    opcion = ""
    while opcion not in ["1","2","3","4","5","6","7"]:
        opcion = input("Elige una categoria (1-7): ")
        if opcion not in ["1","2","3","4","5","6","7"]:
            print("Opcion no valida.")
 
    categoria = categorias[int(opcion) - 1]
 
    # Pedir descripcion
    descripcion = input("Descripcion (Enter para omitir): ")
    if descripcion == "":
        descripcion = "Sin descripcion"
 
    # Crear el gasto
    hoy = str(datetime.date.today())
    gasto = {}
    gasto["fecha"] = hoy
    gasto["cantidad"] = cantidad
    gasto["categoria"] = categoria
    gasto["descripcion"] = descripcion
 
    # Agregar a la lista y guardar
    gastos.append(gasto)
    guardar_datos(gastos)
 
    print("Gasto registrado correctamente!")
    return gastos