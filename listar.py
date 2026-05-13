# listar.py - Muestra los gastos registrados con diferentes filtros.
# El usuario puede ver todos, filtrar por categoria, por hoy o por el mes actual.
 
import datetime
 
# Pregunta al usuario como quiere filtrar y llama a mostrar_lista con el resultado.
def listar_gastos(gastos):
    print("")
    print("===== LISTAR GASTOS =====")
 
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
 
    print("1. Ver todos")
    print("2. Filtrar por categoria")
    print("3. Ver gastos de hoy")
    print("4. Ver gastos de este mes")
 
    opcion = input("Elige una opcion: ")
 
    if opcion == "1":
        mostrar_lista(gastos)
 
    elif opcion == "2":
        categoria = input("Escribe la categoria (comida, transporte, etc): ")
        resultado = []
        for gasto in gastos:
            if gasto["categoria"] == categoria:
                resultado.append(gasto)
        mostrar_lista(resultado)
 
    elif opcion == "3":
        hoy = str(datetime.date.today())
        resultado = []
        for gasto in gastos:
            if gasto["fecha"] == hoy:
                resultado.append(gasto)
        mostrar_lista(resultado)
 
    elif opcion == "4":
        mes = str(datetime.date.today())[0:7]
        resultado = []
        for gasto in gastos:
            if gasto["fecha"][0:7] == mes:
                resultado.append(gasto)
        mostrar_lista(resultado)
 
    else:
        print("Opcion no valida.")
 
# Recibe una lista de gastos ya filtrada y los imprime en pantalla uno por uno.
def mostrar_lista(gastos):
    if len(gastos) == 0:
        print("No hay gastos con ese filtro.")
        return
    print("")
    numero = 1
    for gasto in gastos:
        print(str(numero) + ". Fecha: " + gasto["fecha"] + " | Categoria: " + gasto["categoria"] + " | Cantidad: $" + str(gasto["cantidad"]) + " | " + gasto["descripcion"])
        numero = numero + 1