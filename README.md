# Simulador de Gasto Diario

Aplicación de consola hecha en Python para registrar y monitorear gastos diarios por categorías. Guarda toda la información en un archivo JSON para mantener el historial entre sesiones.

---

## ¿Qué puede hacer?

- Registrar gastos con cantidad, categoría y descripción
- Listar gastos con filtros (por categoría, por hoy, por mes)
- Calcular totales por día, semana, mes o en general
- Generar un reporte y guardarlo en un archivo JSON

---

## Estructura del proyecto

```
├── main.py        # Archivo principal, ejecuta el menú
├── datos.py       # Carga y guarda el archivo JSON
├── registrar.py   # Lógica para registrar un gasto
├── listar.py      # Lógica para listar y filtrar gastos
├── calcular.py    # Lógica para calcular totales
├── reporte.py     # Lógica para generar el reporte
└── gastos.json    # Archivo donde se guardan los gastos
```

---

## Librerías utilizadas

Este proyecto **no necesita instalar nada**. Solo usa librerías que vienen incluidas con Python:

| Librería   | Para qué se usa                                  |
|------------|--------------------------------------------------|
| `json`     | Leer y escribir el archivo JSON con los gastos   |
| `os`       | Verificar si el archivo JSON existe              |
| `datetime` | Obtener la fecha de hoy y calcular rangos de tiempo |

---

## Requisitos

- Python 3.x instalado
- No se necesitan librerías externas ni pip install

---

## Cómo ejecutarlo

1. Descarga o clona el repositorio
2. Asegúrate de que todos los archivos estén en la misma carpeta
3. Abre una terminal en esa carpeta y ejecuta:

```bash
python main.py
```

---

## Ejemplo de uso

```
Bienvenido al Simulador de Gasto Diario
Cargando datos...

========================================
      SIMULADOR DE GASTO DIARIO
========================================
1. Registrar gasto
2. Listar gastos
3. Calcular totales
4. Generar reporte
5. Salir
========================================
Elige una opcion:
```

---

## Formato del archivo gastos.json

Cada gasto se guarda como un objeto con estos campos:

```json
[
    {
        "fecha": "2025-05-13",
        "cantidad": 15000,
        "categoria": "comida",
        "descripcion": "Almuerzo"
    }
]
```

---

## Autor
Achinti Morales Hernández / CampusLands
