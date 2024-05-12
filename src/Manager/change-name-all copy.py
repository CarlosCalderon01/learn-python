import os
import time

def obtener_contador(ruta_contador):
    try:
        with open(ruta_contador, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 1
    except ValueError:
        return 1

def guardar_contador(ruta_contador, contador):
    with open(ruta_contador, 'w') as file:
        file.write(str(contador))

def cambiar_nombres_carpeta(ruta_carpeta, ruta_contador):
    contador = obtener_contador(ruta_contador)

    for ruta_principal, carpetas, archivos in os.walk(ruta_carpeta):
        for nombre_archivo in archivos:
            nombre, formato = os.path.splitext(nombre_archivo)
            ruta_antiguo = os.path.join(ruta_principal, nombre_archivo)
            nombre_nuevo = f"{formato[1:]}_{contador}{formato}"
            ruta_nuevo = os.path.join(ruta_principal, nombre_nuevo)

            os.rename(ruta_antiguo, ruta_nuevo)
            print(f"Renombrado: {nombre_archivo} a {nombre_nuevo}")

            contador += 1
            guardar_contador(ruta_contador, contador)

            time.sleep(0.2)

# Obtener la ubicación del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construir la ruta relativa
ruta_contador = os.path.join(script_dir, "z-contador.txt")

if __name__ == "__main__":
    ruta_carpeta = input("Introduce la ruta de la carpeta: ")
    cambiar_nombres_carpeta(ruta_carpeta, ruta_contador)
