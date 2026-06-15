
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
        print ("\n----- AGREGAR PAIS -----\n")
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
                        print(f"El país '{nuevo_pais.title()}' ya existe en el archivo. Operación cancelada.")
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
def actualizar_datos(ARCHIVO_CSV, datos_actualizados):

    try:
        print("\n----- MODIFICAR PAIS ----- \n")
        #solicitamos el nombre del pais a buscar
        pais_a_buscar = pedir_texto ("Ingrese el nombre del pais que desea actualizar los datos: ").strip().lower()
        #vamos a generar un nuevo dict para poder cargar los datos actualizados
        datos_actualizados = []
        #ponemos las columnas como estan en el csv
        columnas = ['nombre', 'poblacion', 'superficie', 'continente']
        #creamo una bandera para saber si encontramos el pais
        encontrado = False
        
        #Abrimos el archivo en modo lectura
        with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            lector_dict = csv.DictReader(archivo)
            #recorremos todo el archivo
            for fila in lector_dict:
                #comparamos el nombre de la fila con el nombre ingresado
                if fila ['nombre'].lower().strip() == pais_a_buscar:
                    #cambiamos la bandera
                    encontrado = True
                    #mostramos los datos
                    print (f"Pais {pais_a_buscar.title()} encontrado:")
                    print ("Datos almacenados en la base de datos")
                    print (f"Población: {fila['poblacion']} | Superficie: {fila['superficie']} | Continente: {fila['continente']}")

                    #solicitamos los nuevos datos
                    nueva_pob = pedir_int ("\nIngrese la cantidad de habitantes actualizada: ")
                    nueva_sup = pedir_int ("Ingrese la superficie actualizada en km*2: ")

                    #reemplazamos los datos en la fila actual
                    fila['poblacion'] = nueva_pob 
                    fila['superficie'] = nueva_sup 

                #guardamos los datos en la nueva base de datos
                datos_actualizados.append(fila)
        
        #revisamos si se encontro el pais
        if not encontrado:
            print (f"\nEl pais {pais_a_buscar.title()} no se encuentra en la base de datos. si desea ingresarlo utilice la opcion 1.\n")
            return False
        
        #si encontramos el pais sobreescribimos los datos modificados al csv
        elif encontrado:
            with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
                escritor_dict = csv.DictWriter(archivo, fieldnames=columnas)
                #Escribimos las cabeceras de nuevo
                escritor_dict.writeheader()  
                # Escribimos todas las filas juntas
                escritor_dict.writerows(datos_actualizados)
            
            #damos aviso de que realizo la operacion correctamente
            print ("Datos actualizados correctamente.\n")
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

#opcion 3
def buscar_pais (ARCHIVO_CSV, pais_a_buscar):
    try:
        print ("\n------ BUSCAR PAIS -----\n")
        #solicitamos el nombre del pais a buscar
        pais_a_buscar = pedir_texto ("Ingrese el nombre del pais que desea buscar").strip().lower()
        #creamo una bandera para saber si encontramos el pais
        encontrado = False
        
        #Abrimos el archivo en modo lectura
        with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            lector_dict = csv.DictReader(archivo)
            #recorremos todo el archivo
            for fila in lector_dict:
                #comparamos el nombre de la fila con el nombre ingresado
                if fila ['nombre'].lower().strip() == pais_a_buscar:
                    #cambiamos la bandera
                    encontrado = True
                    #mostramos los datos
                    print (f"Pais {pais_a_buscar.title()} encontrado:")
                    print ("Datos almacenados en la base de datos")
                    print (f"Población: {fila['poblacion']} | Superficie: {fila['superficie']} | Continente: {fila['continente']}")
        
        #revisamos si se encontro el pais
        if not encontrado:
            print (f"\nEl pais {pais_a_buscar.title()} no se encuentra en la base de datos. si desea ingresarlo utilice la opcion 1.\n")
            return False
        
    #se crea la validacion por si no se encuentra el archivo CSV
    except FileNotFoundError:
        print (f"El archivo {ARCHIVO_CSV} no se encuentro en la carpeta")
    #verificamos que se pueda trabajar con el csv
    except PermissionError:
        print ("Error. Asegurese que el CSV no se encuentre abierto por otro programa.")
    #Para cualquier otro error lo imprimimos por pantalla
    except Exception as e:
        print (f"Error inesperado: {e}")

