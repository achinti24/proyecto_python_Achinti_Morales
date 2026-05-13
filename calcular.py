# calcular.py - Calcula y muestra el total de gastos por periodo.
# El usuario elige si quiere ver el total de hoy, la semana, el mes o todo.
 
import datetime
 
# Filtra los gastos segun el periodo elegido y llama a mostrar_totales.
def calcular_totales(gastos):
    print("")
    print("===== CALCULAR TOTALES =====")
 
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return
 
    print("1. Total de hoy")
    print("2. Total de esta semana")
    print("3. Total de este mes")
    print("4. Total general")
 
    opcion = input("Elige una opcion: ")
 
    hoy = datetime.date.today()
 
    if opcion == "1":
        hoy_texto = str(hoy)
        filtrados = []
        for gasto in gastos:
            if gasto["fecha"] == hoy_texto:
                filtrados.append(gasto)
        mostrar_totales(filtrados, "HOY")
 
    elif opcion == "2":
        dias_semana = hoy.weekday()
        inicio = hoy - datetime.timedelta(days=dias_semana)
        inicio_texto = str(inicio)
        filtrados = []
        for gasto in gastos:
            if gasto["fecha"] >= inicio_texto:
                filtrados.append(gasto)
        mostrar_totales(filtrados, "ESTA SEMANA")
 
    elif opcion == "3":
        mes = str(hoy)[0:7]
        filtrados = []
        for gasto in gastos:
            if gasto["fecha"][0:7] == mes:
                filtrados.append(gasto)
        mostrar_totales(filtrados, "ESTE MES")
 
    elif opcion == "4":
        mostrar_totales(gastos, "TOTAL GENERAL")
 
    else:
        print("Opcion no valida.")
 
# Suma todos los gastos de la lista recibida y muestra el total y el desglose por categoria.
def mostrar_totales(gastos, titulo):
    print("")
    print("--- Totales: " + titulo + " ---")
 
    if len(gastos) == 0:
        print("No hay gastos en este periodo.")
        return
 
    total = 0
    categorias = {}
 
    for gasto in gastos:
        total = total + gasto["cantidad"]
        cat = gasto["categoria"]
        if cat in categorias:
            categorias[cat] = categorias[cat] + gasto["cantidad"]
        else:
            categorias[cat] = gasto["cantidad"]
 
    print("Total: $" + str(round(total, 2)))
    print("")
    print("Por categoria:")
    for cat in categorias:
        print("  - " + cat + ": $" + str(round(categorias[cat], 2)))