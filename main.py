#Bloque principal
#importamos las funciones desde el archivo utils
import os
from utils import agregar_pais, actualizar_datos, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas
ARCHIVO_CSV = os.path.join(os.path.dirname(__file__), "paises_del_mundo.csv")
#Creamos la variable opcion
opcion = ""
#Creamos menu principal con un bucle while para elergir la opcion deseada
while opcion != 7:
    #Usamos un try except para validar opciones elegidas
    try:
        opcion = int(input ("""\nElija la opcion que necesite (1-7):
1. Agregar pais
2. Actualizar datos de poblacion y superficie de un pais
3. Buscar pais por nombre
4. Filtrar paises
5. Ordenar paises
6. Mostrar estadisticas
7. Salir:

Opcion: """))

        #opcion 1:
        if opcion == 1: 
            agregar_pais(ARCHIVO_CSV)
        #Opcion 2
        elif opcion == 2: 
            actualizar_datos(ARCHIVO_CSV)
        #Opcion 3
        elif opcion == 3: 
            buscar_pais(ARCHIVO_CSV)
        #Opcion 4
        elif opcion == 4: 
            filtrar_paises(ARCHIVO_CSV)
        #Opcion 5
        elif opcion == 5: 
            ordenar_paises(ARCHIVO_CSV)
        #Opcion 6
        elif opcion == 6: 
            mostrar_estadisticas(ARCHIVO_CSV)
        #Opcion 7
        elif opcion == 7:
            #Damos mensaje de salida
            print ("\nGracias por usar el sistema.")
        #Resto de valores
        else:
            print ("\n El numero indicado no pertenece a una opcion válida.\n")

    
    #En caso de ingresar un valor que no coincide usamos un except
    except ValueError:
        print ("\nERROR. Recuerde ingresar solo el numero correspondiente a la opcion deseada (1-7).\n")
    #Como seguridad agregamos una excepcion general
    except Exception as e:
        print (f"\n ERROR INESPERADO: {e}")
