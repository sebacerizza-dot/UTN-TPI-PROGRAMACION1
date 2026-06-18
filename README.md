# UTN-TPI-PROGRAMACION1
TRABAJO PRACTICO INTEGRADOR PROGRAMACION 1 UTN SAN NICOLAS

### Datos del Proyecto
*   **Institución:** Universidad Tecnológica Nacional (UTN) - Facultad Regional San Nicolás
*   **Materia:** Programación I
*   **Comisión:** C22
*   **Profesores:**
    *   Cinthia Rigoni
    *   Martín A. García
    *   Ariel Enferrel
*   **Tutores:**
    *   Neyén Bianchi      
*   **Integrantes:** 
    *   Sebastian Cerizza
    *   Maximiliano Castillo

*   **Video:** 
https://youtu.be/zDyY6cwO5E0

Este proyecto consiste en una aplicación de consola desarrollada en Python para la administración, filtrado y análisis estadístico de un registro global de países. El sistema implementa persistencia de datos local mediante un archivo de texto plano en formato CSV (`paises_del_mundo.csv`).

El desarrollo cumple con los lineamientos de modularización requeridos, separando la interfaz de interacción con el usuario de la lógica interna de procesamiento y validación de archivos.

---

## Estructura del Proyecto

El programa se divide en los siguientes componentes:

*   **Script Principal (`main.py`):** Contiene el bucle de control (`while`) que despliega el menú interactivo con las 7 opciones del sistema. Implementa bloques `try-except` globales para capturar ingresos inválidos y asegurar que el programa no finalice de forma inesperada.
*   **Módulo de Utilidades (`utils.py`):** Concentra la lógica del programa, incluyendo las funciones de lectura/escritura del CSV, los algoritmos de ordenamiento y filtrado, y las capas de estadísticas.
*   **Base de Datos (`paises_del_mundo.csv`):** Almacena los registros estructurados bajo las columnas `nombre`, `poblacion`, `superficie` y `continente`.

```text
UTN-TPI-PROGRAMACION1/
│
├── main.py                    # Script principal. Maneja el menú interactivo y control de errores global.
├── utils.py                   # Módulo de utilidades. Contiene las funciones de lógica y validaciones.
└── paises_del_mundo.csv       # Base de datos local en texto plano (formato CSV).
```

---

## Características Principales

1.  **Gestión de Registros:** Alta de nuevos países (verificando previamente que no existan duplicados) y actualización de las variables numéricas de población y superficie de los países registrados.
2.  **Búsqueda Unitaria:** Localización y muestra de datos estructurados buscando directamente por el nombre del país.
3.  **Filtrados Avanzados:** Filtrado por coincidencia de continente o mediante la especificación de rangos numéricos inclusivos (mínimos y máximos) para población y km².
4.  **Ordenamiento Dinámico:** Reorganización de las listas en pantalla bajo criterios alfabéticos o numéricos, permitiendo definir el sentido (ascendente o descendente) según el campo seleccionado.
5.  **Módulo Estadístico:** Procesamiento de datos en memoria para calcular el promedio global de habitantes y superficies, detección de países extremos (máxima y mínima población), y un conteo agrupado por frecuencias de países por cada continente.

---

## Validaciones Implementadas

El sistema fue diseñado bajo el principio de programación defensiva para mitigar fallas en tiempo de ejecución:

*   **Validación de Entradas:** Funciones de captura encargadas de rechazar cadenas vacías o espacios redundantes, así como de forzar la entrada de valores numéricos enteros dentro de límites lógicos aceptables.
*   **Parseo Seguro de Datos:** El lector (`DictReader`) procesa el archivo fila por fila. En caso de detectar valores corruptos o campos de texto donde debería haber números, el bloque `try-except` interno asigna valores seguros por defecto (`0`) en lugar de interrumpir la ejecución.
*   **Manejo de Excepciones del Entorno:** Control explícito de errores de E/S, tales como la ausencia física del archivo (`FileNotFoundError`) o bloqueos por derechos de escritura (`PermissionError`) comunes cuando el archivo CSV se encuentra abierto en un programa externo como Excel.

---
## Librerías
La aplicación no requiere la instalación de librerías de terceros. El sistema fue desarrollado utilizando puramente las herramientas nativas de la Librería Estándar de Python:

*   **csv: Para la lectura y escritura estructurada mediante diccionarios (DictReader y DictWriter).**
*   **os: Para la verificación de existencia física de archivos en el disco de manera multiplataforma.**

---

## Instrucciones de Uso

Para poner en marcha la aplicación de consola, ejecute el script del menú principal desde la terminal de su entorno de desarrollo:

```bash
python main.py
```
---

## Ejemplos de Entrada y Salida
Ejemplo 1: Búsqueda Exitosa (Opción 3)
*  **Entrada del usuario:**
```
Elija la opcion que necesite (1-7): 3
Ingrese el nombre del pais que desea buscar: argentina
```
* **Salida del sistema:**
```
Pais Argentina encontrado:
  Datos almacenados en la base de datos
  Población: 45376763 | Superficie: 2780400 | Continente: América
```
