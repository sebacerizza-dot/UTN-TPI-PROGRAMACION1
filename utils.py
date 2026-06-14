
import csv
import os

ARCHIVO_CSV = "paises_del_mundo.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

#Validacion para ingresar int
def pedir_int(mensaje, minimo=0, maximo=None):
    while True:
        try:
            val = int(input(mensaje))
            if val < minimo:
                print(f" ERROR. Debe ser ≥ {minimo}.")
            elif maximo is not None and val > maximo:
                print(f" ERROR. No puede superar el límite lógico de {maximo}.")
            else:
                return val
        except ValueError:
            print(" ERROR. Ingresá un número entero.")

#Validacion para ingresar string
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print(" ERROR. No puede quedar vacío.")

#Opcion 1:
def agregar_pais(ARCHIVO_CSV, nuevo_pais):
    try:
        #solicitamos el pais a agregar
        print ("\nagregar pais:\n")
        pais_a_agregar = pedir_texto("Ingrese el nombre del pais a agregar: ")
        #lo pasamos a minusculas y eliminamos cualquier espacio o indentacion que haya quedado
        nuevo_pais = pais_a_agregar.lower().strip()
        #verificamos que exista el archivo csv
        if os.path.exists(ARCHIVO_CSV):
            #abrimos el archivo csv en modo lectura
            with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
                #leemos el archivo como un diccionario para poder utilizar el encabezado
                lector_dict = csv.DictReader(archivo)
                for fila in lector_dict:
                # Comparamos directamente usando el nombre de la columna
                    if fila['nombre'].lower().strip() == nuevo_pais:
                        print(f"El país '{nuevo_pais}' ya existe en el archivo. Operación cancelada.")
                        return False
    
            # Si no existe, pide la informacion para agregarlo
            print (f"{pais_a_agregar} no se encuentra registrado. ingrese los siguientes datos:")
            pob = pedir_int ("Ingrese la cantidad de habitantes: ")
            sup = pedir_int ("Ingrese la superficie en Km*2: ")
            #para ingresar el continente creamos un menu para asegurar que usen los nombres que deseamos
            
            continentes = ["América", "Europa", "Asia", "Oceanía", "África"]

            while True:
                print("\nSeleccione el continente:")
                print("1. América")
                print("2. Europa")
                print("3. Asia")
                print("4. Oceanía")
                print("5. África")
                #solicitamos el numero de la opcion deseada
                opcion = pedir_int("\nElija la opcion deseada (1-5): ").strip()

                #Validamos la opcion
                if opcion in [1, 2, 3, 4, 5]:
                    #usamos el numero para elegir la opcion deseada
                    cont = continentes [opcion-1]
                    break #salimos del bucle
                #sino damos mensaje de error
                else:
                    print ("Valor ingresado invalido. ingrese el numero de acuerdo a la opcion deseada (1-5).")

            #armamos el dicionario con los datos ingresados
            
            nuevo_pais_dict = {'nombre': nuevo_pais.title(), 'poblacion': pob, 'superficie': sup, 'continente': cont}

            # Si el archivo es nuevo, escribirá las cabeceras primero
            archivo_existe = os.path.exists(ARCHIVO_CSV)
            
            with open(ARCHIVO_CSV, mode='a', newline='', encoding='utf-8') as archivo:
                # Definimos el orden exacto de las columnas de tu CSV
                colmunas = ['nombre', 'poblacion', 'superficie', 'continente']
                escritor_dict = csv.DictWriter( ARCHIVO_CSV, fieldnames=colmunas)
                
                # Si el archivo se está creando de cero, escribimos los nombres de las columnas
                if not archivo_existe:
                    escritor_dict.writeheader()
                    
                # Escribimos el diccionario completo como una nueva fila
                escritor_dict.writerow(nuevo_pais_dict)
                print(f"¡{nuevo_pais.title()}! agregado con éxito al CSV.")
                return True
    #Si bien ya estan validadas las funciones donde se ingresan los datos. Se deja el except para mostrar como se usa
    except ValueError:
        print ("Error. ingrese un numero entero")
    #se crea la validacion por si no se encuentra el archivo CSV
    except FileNotFoundError:
        print (f"El archivo {ARCHIVO_CSV} no se encuentro en la carpeta")
    #verificamos que se pueda trabajar con el csv
    except PermissionError:
        print ("Error. Asegurese que el CSV no se encuentre abierto por otro programa.")
    #Para cualquier otro error lo imprimimos por pantalla
    except Exception as e:
        print (f"Error inesperado: {e}")

#opcion 2