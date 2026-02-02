# Sistema de Registro de Ventas (Python & CSV)

Este es un sistema de gestión de ventas desarrollado en **Python** que utiliza archivos **CSV** para la persistencia de datos. El proyecto fue diseñado con un enfoque en la integridad de los datos y el manejo eficiente de archivos planos, simulando la lógica de una base de datos relacional.

## Características

- **Registro de Ventas:** Captura de datos con validación de tipos.
- **Persistencia en CSV:** Los datos se almacenan en `csv_data/archivo_ventas.csv`. El sistema crea automáticamente las carpetas y los encabezados si no existen.
- **Lógica de ID Autoincremental:** Al iniciar, el programa escanea el archivo CSV para recuperar el último ID y continuar la secuencia para evitar IDs duplicados.
- **Reportes Dinámicos:** Cálculo automático de subtotales, promedios de venta y ganancias totales.
- **Edición y Borrado:** Localización de registros mediante búsqueda por ID y actualización de archivos.

## Tecnologías utilizadas

- **Lenguaje:** Python 3.x
- **Módulos Nativos:** 
  - `csv`: Para la manipulación de datos estructurados.
  - `os`: Para la gestión de rutas y directorios de forma independiente al Sistema Operativo.
  - `sys`: Para el correcto funcionamiento de las rutas.

## Arte ASCII sacado de: https://ascii.co.uk/art/walrus

## Cómo usar el script sin el ejecutable (podria causar errores)

1. Clonar el repositorio.
2. Asegúrarse de tener Python 3.0 instalado.
3. Ejecutar el script principal:
   ```bash
   python intento1_data.py
