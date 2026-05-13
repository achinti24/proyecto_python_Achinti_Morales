# reporte.py - Genera un resumen de gastos por dia, semana y mes.
# Al final pregunta si el usuario quiere guardar el reporte en un archivo JSON.

import datetime
import json

# Calcula los totales de todos los periodos y muestra el reporte en pantalla.
# Si el usuario confirma, guarda el reporte en un archivo JSON con la fecha en el nombre.
def generar_reporte(gastos):
    print("")
    print("===== GENERAR REPORTE =====")

    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return

    hoy = datetime.date.today()
    hoy_texto = str(hoy)
    mes = hoy_texto[0:7]
    dias_semana = hoy.weekday()
    inicio_semana = str(hoy - datetime.timedelta(days=dias_semana))

    # Calcular totales
    total_hoy = 0
    total_semana = 0
    total_mes = 0
    categorias_mes = {}

    for gasto in gastos:
        if gasto["fecha"] == hoy_texto:
            total_hoy = total_hoy + gasto["cantidad"]
        if gasto["fecha"] >= inicio_semana:
            total_semana = total_semana + gasto["cantidad"]
        if gasto["fecha"][0:7] == mes:
            total_mes = total_mes + gasto["cantidad"]
            cat = gasto["categoria"]
            if cat in categorias_mes:
                categorias_mes[cat] = categorias_mes[cat] + gasto["cantidad"]
            else:
                categorias_mes[cat] = gasto["cantidad"]

    # Mostrar reporte en pantalla
    print("")
    print("========================================")
    print("           REPORTE DE GASTOS")
    print("  Fecha: " + hoy_texto)
    print("========================================")
    print("  Gasto de hoy:       $" + str(round(total_hoy, 2)))
    print("  Gasto esta semana:  $" + str(round(total_semana, 2)))
    print("  Gasto este mes:     $" + str(round(total_mes, 2)))
    print("----------------------------------------")
    print("  Desglose mensual por categoria:")
    for cat in categorias_mes:
        print("    - " + cat + ": $" + str(round(categorias_mes[cat], 2)))
    print("  Total de registros: " + str(len(gastos)))
    print("========================================")

    # Preguntar si guardar
    respuesta = input("Guardar reporte en archivo? (s/n): ")
    if respuesta == "s":
        nombre = "reporte_" + hoy_texto + ".json"
        datos_reporte = {}
        datos_reporte["fecha"] = hoy_texto
        datos_reporte["total_hoy"] = round(total_hoy, 2)
        datos_reporte["total_semana"] = round(total_semana, 2)
        datos_reporte["total_mes"] = round(total_mes, 2)
        datos_reporte["categorias_mes"] = categorias_mes
        datos_reporte["total_registros"] = len(gastos)

        archivo = open(nombre, "w")
        json.dump(datos_reporte, archivo)
        archivo.close()
        print("Reporte guardado como: " + nombre)
    else:
        print("Reporte no guardado.")