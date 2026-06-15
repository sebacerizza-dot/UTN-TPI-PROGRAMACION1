# UTN-TPI-PROGRAMACION1
TRABAJO PRACTICO INTEGRADOR PROGRAMACION 1 UTN SAN NICOLAS

Este proyecto consiste en una aplicación de consola desarrollada en Python para la administración, filtrado y análisis estadístico de un registro global de países. El sistema implementa persistencia de datos local mediante un archivo de texto plano en formato CSV (`paises_del_mundo.csv`)[cite: 1, 2].

El desarrollo cumple con los lineamientos de modularización requeridos, separando la interfaz de interacción con el usuario de la lógica interna de procesamiento y validación de archivos[cite: 1, 2].

---

## Estructura del Código

El programa se divide en los siguientes componentes:

*   **Script Principal (`main.py`):** Contiene el bucle de control (`while`) que despliega el menú interactivo con las 7 opciones del sistema[cite: 2]. Implementa bloques `try-except` globales para capturar ingresos inválidos y asegurar que el programa no finalice de forma inesperada[cite: 2].
*   **Módulo de Utilidades (`utils.py`):** Concentra la lógica del negocio, incluyendo las funciones de lectura/escritura del CSV, los algoritmos de ordenamiento y filtrado, y las capas de estadísticas[cite: 1, 2].
*   **Base de Datos (`paises_del_mundo.csv`):** Almacena los registros estructurados bajo las columnas `nombre`, `poblacion`, `superficie` y `continente`[cite: 1].

---

## Características Principales

1.  **Gestión de Registros:** Alta de nuevos países (verificando previamente que no existan duplicados) y actualización de las variables numéricas de población y superficie de los países registrados[cite: 1].
2.  **Búsqueda Unitaria:** Localización y muestra de datos estructurados buscando directamente por el nombre del país[cite: 1].
3.  **Filtrados Avanzados:** Filtrado por coincidencia de continente o mediante la especificación de rangos numéricos inclusivos (mínimos y máximos) para población y km²[cite: 1].
4.  **Ordenamiento Dinámico:** Reorganización de las listas en pantalla bajo criterios alfabéticos o numéricos, permitiendo definir el sentido (ascendente o descendente) según el campo seleccionado[cite: 1].
5.  **Módulo Estadístico:** Procesamiento de datos en memoria para calcular el promedio global de habitantes y superficies, detección de países extremos (máxima y mínima población), y un conteo agrupado por frecuencias de países por cada continente[cite: 1].

---

## Validaciones Implementadas

El sistema fue diseñado bajo el principio de programación defensiva para mitigar fallas en tiempo de ejecución:

*   **Validación de Entradas:** Funciones de captura encargadas de rechazar cadenas vacías o espacios redundantes, así como de forzar la entrada de valores numéricos enteros dentro de límites lógicos aceptables[cite: 1].
*   **Parseo Seguro de Datos:** El lector (`DictReader`) procesa el archivo fila por fila[cite: 1]. En caso de detectar valores corruptos o campos de texto donde debería haber números, el bloque `try-except` interno asigna valores seguros por defecto (`0`) en lugar de interrumpir la ejecución[cite: 1].
*   **Manejo de Excepciones del Entorno:** Control explícito de errores de E/S, tales como la ausencia física del archivo (`FileNotFoundError`) o bloqueos por derechos de escritura (`PermissionError`) comunes cuando el archivo CSV se encuentra abierto en un programa externo como Excel[cite: 1].

---

## Instrucciones de Uso

Para poner en marcha la aplicación de consola, ejecute el script del menú principal desde la terminal de su entorno de desarrollo:

```bash
python main.py
