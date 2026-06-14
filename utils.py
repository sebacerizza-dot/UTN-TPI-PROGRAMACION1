def pedir_int(mensaje, minimo=0, maximo=None):
    while True:
        try:
            val = int(input(mensaje))
            if val < minimo:
                print(f"  ⚠ Debe ser ≥ {minimo}.")
            elif maximo is not None and val > maximo:
                print(f"  ⚠ No puede superar el límite lógico de {maximo}.")
            else:
                return val
        except ValueError:
            print("  ⚠ Ingresá un número entero.")

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  ⚠ No puede quedar vacío.")
