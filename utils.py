
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

def lee_archivo(ARCHIVO_CSV):
    datos_limpios = []
    with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
        # Al no pasarle fieldnames, DictReader toma la primera línea automáticamente como claves
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            # 1. Validación estricta: nos aseguramos de que sea un diccionario válido
            if not isinstance(fila, dict) or not fila:
                continue  # Saltea líneas vacías o corruptas
                
            # 2. Convertir Población a entero de forma segura
            try:
                fila['poblacion'] = int(fila['poblacion'])
            except (ValueError, TypeError, KeyError):
                fila['poblacion'] = 0

            # 3. Convertir Superficie a entero de forma segura
            try:
                fila['superficie'] = int(fila['superficie'])
            except (ValueError, TypeError, KeyError):
                fila['superficie'] = 0

            # Agregamos el país procesado a nuestra lista
            datos_limpios.append(fila)

        return datos_limpios

#Opcion 1:
def agregar_pais(ARCHIVO_CSV):
    try:
        #solicitamos el pais a agregar
        print ("\n----- AGREGAR PAIS -----\n")
        pais_a_agregar = pedir_texto("Ingrese el nombre del pais a agregar: ")
        #lo pasamos a minusculas y eliminamos cualquier espacio o indentacion que haya quedado
        nuevo_pais = pais_a_agregar.lower().strip()
        #verificamos que exista el archivo csv
        if os.path.exists(ARCHIVO_CSV):
            #abrimos el archivo csv en modo lectura
            # with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            #     #leemos el archivo como un diccionario para poder utilizar el encabezado
            #     lector_dict = csv.DictReader(archivo)
            lector_dict=lee_archivo(ARCHIVO_CSV)
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
                opcion = pedir_int("\nElija la opcion deseada (1-5): ")

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
                escritor_dict = csv.DictWriter( archivo, fieldnames=colmunas)
                
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
def actualizar_datos(ARCHIVO_CSV):

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
        # with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
        #     lector_dict = csv.DictReader(archivo)
        lector_dict=lee_archivo(ARCHIVO_CSV)
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
def buscar_pais (ARCHIVO_CSV):
    try:
        print ("\n------ BUSCAR PAIS -----\n")
        #solicitamos el nombre del pais a buscar
        pais_a_buscar = pedir_texto ("Ingrese el nombre del pais que desea buscar: ").strip().lower()
        #creamo una bandera para saber si encontramos el pais
        encontrado = False
        
        #Abrimos el archivo en modo lectura
        # with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
        #     lector_dict = csv.DictReader(archivo)
        lector_dict=lee_archivo(ARCHIVO_CSV)
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

#opcion 4
def filtrar_paises (ARCHIVO_CSV):
    #generamos un sub menu para elgir la opcion que quiera utilizar
    print ("""\n----- FILTAR PAISES ----- 
Seleccione la opcion que desee utiliza:
1) Filtrar por continente.
2) Filtrar por rango de poblacion.
3) Filtrar por rango de superficie.
""")
    opcion = pedir_int ("Ingrese el numero correspondiente a la opcion deseada (1-3): ")
    #opcion 1
    if opcion == 1:
        try:
            #Generamos un menu para que elija el continente
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
                opcion = pedir_int("\nElija la opcion deseada (1-5): ")

                #Validamos la opcion
                if opcion in [1, 2, 3, 4, 5]:
                    #usamos el numero para elegir la opcion deseada
                    cont = continentes [opcion-1]
                    break #salimos del bucle
                #sino damos mensaje de error
                else:
                    print ("Valor ingresado invalido. ingrese el numero de acuerdo a la opcion deseada (1-5).")
            #avisamos que continente de a seleccionado
            print (f"\nContinente elegido: {cont}")
            #Abrimos el archivo en modo lectura
            # with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            #     lector_dict = csv.DictReader(archivo)
            lector_dict=lee_archivo(ARCHIVO_CSV)
            #recorremos todo el archivo
            for fila in lector_dict:
                #comparamos el nombre de la fila con el nombre ingresado
                if fila ['continente'] == cont:
                    #imprimimos esa fila
                    print (f"-Pais: {fila['nombre']}  Poblacion: {fila['poblacion']}  Superficie: {fila['superficie']} km*2")
            
            #damos aviso de proceso finalizado
            print ("\nProceso terminado.\n")
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
    elif opcion == 2:
        #solicitamos el numero de poblacion minima
        poblacion_min = pedir_int ("Ingrese el la cantidad minima de poblacion: ")
        #solicitamos el numero de poblacion maxima
        poblacion_max = pedir_int ("Ingrese el la cantidad maxima de poblacion: ")
        #generamos una bandera
        dentro_rango = False

        #damos mensaje de filtro
        print (f"\nPaises filtrados por rango de poblacion ({poblacion_min}-{poblacion_max}).\n")
        try:
            #Abrimos el archivo en modo lectura
            # with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            #     lector_dict = csv.DictReader(archivo)
            lector_dict=lee_archivo(ARCHIVO_CSV)
            #recorremos todo el archivo
            for fila in lector_dict:
                poblacion_fila = int (fila['poblacion'])
                #comparamos el valor de la fila con los valores ingresados
                if poblacion_fila <= poblacion_max and poblacion_fila >= poblacion_min:
                    #cambiamos la bandera
                    dentro_rango = True
                    #imprimimos los datos
                    print (f"-Pais: {fila['nombre']}  Poblacion: {fila['poblacion']}  Superficie: {fila['superficie']} km*2  Continente: {fila['continente']}")

            #si no hay ningun pais dentro del rango dado damos mensaje
            if not dentro_rango:
                print ("No hay nigun pais dentro del rango especificado.")
                return False
            #damos aviso de proceso finalizado
            print ("\nProceso terminado.\n")
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
    elif opcion == 3:
        #solicitamos el numero de poblacion minima
        superficie_min = pedir_int ("Ingrese el la cantidad minima de superficie: ")
        #solicitamos el numero de poblacion maxima
        superficie_max = pedir_int ("Ingrese el la cantidad maxima de superficie: ")
        #generamos una bandera
        dentro_rango = False

        #damos mensaje de filtro
        print (f"\nPaises filtrados por rango de superficie ({superficie_min}-{superficie_max}) Km*2.\n")
        try:
            #Abrimos el archivo en modo lectura
            # with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            #     lector_dict = csv.DictReader(archivo)
            lector_dict=lee_archivo(ARCHIVO_CSV)
            #recorremos todo el archivo
            for fila in lector_dict:
                superficie_fila = int (fila['superficie'])
                #comparamos el valor de la fila con los valores ingresados
                if superficie_fila <= superficie_max and superficie_fila >= superficie_min:
                    #cambiamos la bandera
                    dentro_rango = True
                    #imprimimos los datos
                    print (f"-Pais: {fila['nombre']}  Poblacion: {fila['poblacion']}  Superficie: {fila['superficie']} km*2  Continente: {fila['continente']}")

            #si no hay ningun pais dentro del rango dado damos mensaje
            if not dentro_rango:
                print ("No hay nigun pais dentro del rango especificado.")
                return False
            #damos aviso de proceso finalizado
            print ("\nProceso terminado.\n")
            #se crea la validacion por si no se encuentra el archivo CSV
        except FileNotFoundError:
            print (f"El archivo {ARCHIVO_CSV} no se encuentro en la carpeta")
        #verificamos que se pueda trabajar con el csv
        except PermissionError:
            print ("Error. Asegurese que el CSV no se encuentre abierto por otro programa.")
        #Para cualquier otro error lo imprimimos por pantalla
        except Exception as e:
            print (f"Error inesperado: {e}")
    else:
        print ("Error. Debe ingresar un valor en el rango indicado (1-3).")

def ordenar_paises(ARCHIVO_CSV):
    # Inicializa la variable de control del menú interactivo
    opcion=-1
    
    # Bucle principal que se ejecuta hasta que el usuario elija salir (0)
    while opcion!=0:
        # Muestra en pantalla las opciones del menú de ordenamiento
        print("1)Nombre")
        print("2)Población")
        print("3)Superficie")
        print("0)Salir")

        # Solicita y valida la opción del usuario (debe ser un entero entre 0 y 3)
        opcion=pedir_int("ingrese el numero de la opcion elegida para el campo de ordenamiento: ",0,3)
        
        # Si el usuario elige 0, imprime una línea en blanco y finaliza el bucle
        if opcion==0:
            print("")
        else:
            # Configura las variables si se elige ordenar por nombre
            if opcion==1:
                campo="nombre"  # Nombre de la clave en el diccionario
                tipo=str        # Tipo de dato para la comparación (texto)
                orden=False     # False significa orden ascendente (A-Z)
                
            # Configura las variables si se elige ordenar por población
            elif opcion==2:
                campo="poblacion" # Nombre de la clave en el diccionario
                tipo=int          # Tipo de dato para la comparación (numérico)
                orden=False       # False significa de menor a mayor
                
            # Configura las variables si se elige ordenar por superficie
            elif opcion==3:
                campo="superficie" # Nombre de la clave en el diccionario
                tipo=int           # Tipo de dato para la comparación (numérico)
                
                # Muestra submenú para elegir el sentido de la ordenación
                print("1) ascendente")
                print("2) descendente")
                
                # Si el usuario elige una opción distinta de 1, invierte el orden (descendente)
                if pedir_int("ingrese el numero de la opcion elegida para sentido del ordenamiento: ",1,2)!=1:
                    orden=True     # True activa el orden descendente
                else:
                    orden=False    # False mantiene el orden ascendente
                    
            # Carga la lista de diccionarios desde el archivo CSV externo
            datos=lee_archivo(ARCHIVO_CSV)

            # Ordena la lista usando una función lambda que convierte el campo al tipo de dato correspondiente
            datos.sort(key=lambda x: tipo(x[campo]), reverse=orden )

            # Recorre la lista ya ordenada e imprime los datos de cada país en la consola
            for fila in datos:
                print(fila['nombre'], fila['poblacion'], fila['superficie'], fila['continente'])


def mostrar_estadisticas(ARCHIVO_CSV):
    # Inicializa la variable de control del menú interactivo
    opcion=-1
    
    # Bucle principal que se ejecuta hasta que el usuario decida salir (0)
    while opcion!=0:
        # Muestra en pantalla las opciones disponibles del menú de estadísticas
        print("1)País con mayor y menor población")
        print("2)Promedio de población")
        print("3)Promedio de superficie")
        print("4)Cantidad de países por continente")
        print("0)Salir")
        # Solicita y valida la opción del usuario (debe ser un entero entre 0 y 4)
        opcion=pedir_int("ingrese el numero de la opcion elegida: ",0,4)
        
        # OPCIÓN 1: Encontrar los extremos de población
        if opcion==1:
            datos=lee_archivo(ARCHIVO_CSV) # Carga los datos del archivo
            
            # Ordena los países de mayor a menor población convirtiendo el valor a entero
            datos.sort(key=lambda x: int(x["poblacion"]), reverse=True )
            
            # El primer elemento de la lista ordenada es el país más poblado
            primer_pais = datos[0]
            print(f"El país con mayor población es: {primer_pais['nombre']} con una población de {primer_pais['poblacion']} habitantes")
            
            # Invierte el orden de la lista (ahora queda de menor a mayor)
            datos.reverse()
            
            # Toma el nuevo primer elemento, que corresponde al país menos poblado
            ultimo_pais = datos[0]
            print(f"El país con menor población es: {ultimo_pais['nombre']} con una población de {ultimo_pais['poblacion']} habitantes")
            
        # OPCIÓN 2: Calcular el promedio de población
        if opcion==2:
            datos=lee_archivo(ARCHIVO_CSV) # Carga los datos del archivo
            contador=0                     # Cuenta la cantidad de registros
            acumulador=0                   # Suma las poblaciones totales
            
            # Recorre cada país sumando los habitantes y contando el elemento
            for pais in datos:
                contador+=1
                acumulador+=pais['poblacion'] # Nota: Puede requerir int(pais['poblacion']) si el CSV lee texto
                
            # Calcula e imprime el promedio dividiendo el total por la cantidad
            print(f"el promedio de poblacion es {acumulador/contador}")
            
        # OPCIÓN 3: Calcular el promedio de superficie
        if opcion==3:
            datos=lee_archivo(ARCHIVO_CSV) # Carga los datos del archivo
            contador=0                     # Cuenta la cantidad de registros
            acumulador=0                   # Suma las superficies totales
            
            # Recorre cada país sumando los kilómetros cuadrados y contando el elemento
            for pais in datos:
                contador+=1
                acumulador+=pais['superficie'] # Nota: Puede requerir int(pais['superficie']) si el CSV lee texto
                
            # Calcula e imprime el promedio dividiendo la superficie total por la cantidad
            print(f"el promedio de superficie es {acumulador/contador}")
            
        # OPCIÓN 4: Agrupar y contar países por continente
        if opcion==4:
            agrupado={}                    # Diccionario para almacenar las frecuencias {continente: cantidad}
            datos=lee_archivo(ARCHIVO_CSV) # Carga los datos del archivo
            
            # Recorre todos los registros del archivo
            for registro in datos:
                registro['continente']     # Accede al campo (esta línea no altera los datos ni asigna variables)
                
                # Busca si el continente ya está registrado en el diccionario
                resultado = agrupado.get(registro['continente'])
                
                # Si no existe, lo agrega al diccionario inicializando su contador en 1
                if resultado==None:
                    agrupado[registro['continente']]=1
                # Si ya existe, incrementa su contador en 1
                else:
                    agrupado[registro['continente']]+=1
                    
            # Muestra en la consola los totales calculados para cada continente
            for continente, cantidad in agrupado.items():
                print(f"{continente}: {cantidad} países")
