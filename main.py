#Version1.1.
import os
import requests


print("Nueva version prueba automáticamente desde GitHub Actions")

print("TOKEN:", os.getenv("GITHUB_TOKEN"))
app_json = "application/vnd.github+json"
url_consulta = "https://api.github.com/repos/Marianoya/fase2devops/dispatches"

def notificar_consulta(nombre_cliente):
    token = os.getenv("GITHUB_TOKEN")
    url = url_consulta
    headers = {
        "Accept": app_json,
        "Authorization": f"Bearer {token}"
    }
    data = {
        "event_type": "consulta_cliente",
        "client_payload": {
            "cliente": nombre_cliente
        }
    }
    requests.post(url, json=data, headers=headers)

def consultar_mejoras(nombre_mejora):
    token = os.getenv("GITHUB_TOKEN")
    url = url_consulta
    headers = {
        "Accept": app_json,
        "Authorization": f"Bearer {token}"
    }
    data = {
        "event_type": "consulta_mejora",
        "client_payload": {
            "mejora": nombre_mejora
        }  }
    requests.post(url, json=data, headers=headers)
def notificar_funcion(nombre_funcion):
    token = os.getenv("GITHUB_TOKEN")
    url = url_consulta
    headers = {
        "Accept": app_json,
        "Authorization": f"Bearer {token}"
    }
    data = {
        "event_type": "consulta_funciones",
        "client_payload": {
            "funcion": nombre_funcion
        }}
    requests.post(url, json=data, headers=headers)


# Cargar clientes existentes al iniciar

# Diccionario (tabla hash)
# clave: nombre del cliente
# valor: ruta del archivo
clientes = {}

CARPETA_CLIENTES = "clientes"

if not os.path.exists(CARPETA_CLIENTES):
    os.makedirs(CARPETA_CLIENTES)

for archivo in os.listdir(CARPETA_CLIENTES):
    if archivo.endswith(".txt"):
        nombre = archivo.replace(".txt", "")
        clientes[nombre] = f"{CARPETA_CLIENTES}/{archivo}"
    

def crear_cliente():
    nombre = input("Ingresa el Nombre del cliente: ")
    ruta = f"clientes/{nombre}.txt"

    if os.path.exists(ruta):
        print("El cliente ya existe. No se puede crear nuevamente.")
        return

    servicio = input("Ingresa Servicio solicitado por el cliente: ")
    archivo = f"{CARPETA_CLIENTES}/{nombre.replace(' ', '_')}.txt"

    with open(archivo, "w") as f:
        f.write(f"Cliente: {nombre}\n")
        f.write(f"Servicio: {servicio}\n")

    clientes[nombre] = archivo
    print("Cliente creado correctamente.")


def consultar_cliente():

    nombre = input("Ingresa Nombre del cliente para visulizar los servicios solicitados: ")

    if nombre not in clientes:
            print("Cliente no encontrado en la base de datos.")
            return

    with open(clientes[nombre], "r") as f:
            print("\n--- Información del cliente ---")
            print(f.read())
    
    notificar_consulta(nombre)

def consultar_lista():
    
    print("\n--- Lista de clientes registrados ---")
    for nombre, archivo in clientes.items():
        print(f"Nombre del cliente: {nombre}")    

    print("\n--- Lista de clientes registrados en diccionario ---")
    for nombre, archivo in clientes.items():
        print(f"Nombre (Key): {nombre} | Ruta/Value del Key: {archivo}")
        
    if len(clientes) == 0:
            print("No hay registro de datos por el momento.")
            print("Primero registre en la opcion 1 al menos un cliente con su servicio")
            
    notificar_consulta("lista completa de clientes")
    
def actualizar_cliente():
    nombre = input("Ingresa Nombre del cliente para agregar servicio(s): ")
    ruta = f"clientes/{nombre}.txt"

    if not os.path.exists(ruta):
        print("El cliente no existe. No se puede modificar.")
        return

    nuevo_servicio = input("Nuevo servicio solicitado por el cliente: ")

    with open(clientes[nombre], "a") as f:
        f.write(f"Servicio adicional: {nuevo_servicio}\n")

    print("Cliente actualizado correctamente.")


def borrar_cliente():
    nombre = input("Ingresa el Nombre del cliente a eliminar: ")

    if nombre not in clientes:
        print("Cliente no encontrado en la base de datos.")
        return

    os.remove(clientes[nombre])
    del clientes[nombre]

    print("Cliente eliminado correctamente de la base de datos.")


mejoras = {}
CARPETA_MEJORAS = "mejoras"
if not os.path.exists(CARPETA_MEJORAS):
    os.makedirs(CARPETA_MEJORAS)
for archivo_mejora in os.listdir(CARPETA_MEJORAS):
    if archivo_mejora.endswith(".txt"):
        nombre_mejora = archivo_mejora.replace(".txt", "")
        mejoras[nombre_mejora] = f"{CARPETA_MEJORAS}/{archivo_mejora}"
def registrar_mejora():
    nombre_mejora = input("Ingresa la mejora para la aplicacion: ")
    ruta = f"mejoras/{nombre_mejora}.txt"
    if os.path.exists(ruta):
        print("La mejora propuesta ya existe. No se puede crear nuevamente.")
        return
    servicio_mejora = input("Ingresa Servicio solicitado a mejorar: ")
    archivo_mejora = f"{CARPETA_MEJORAS}/{nombre_mejora.replace(' ', '_')}.txt"
    with open(archivo_mejora, "w") as f:
        f.write(f"Mejora: {nombre_mejora}\n")
        f.write(f"Servicio de la aplicacion a mejorar: {servicio_mejora}\n")
    mejoras[nombre_mejora] = archivo_mejora
    print("Mejora registrada correctamente.")
def modificar_codigo():
    nombre_mejora = input("Ingresa Nombre de la mejora para modificar el código de la aplicación: ")
    ruta = f"mejoras/{nombre_mejora}.txt"
    if not os.path.exists(ruta):
        print("La mejora no existe. No se puede modificar.")
        return
    nuevo_status = input("Nuevo estado de la mejora: ")
    with open(mejoras[nombre_mejora], "a") as f:
        f.write(f"Nuevo estado: {nuevo_status}\n")
    print("Mejora actualizada correctamente.")

def mostrar_mejoras():
    nombre_mejora = input("Ingresa Nombre de la mejora para visualizar: ")

    if nombre_mejora not in mejoras:
        print("Mejora no encontrada en la base de datos.")
        return

    with open(mejoras[nombre_mejora], "r") as f:
            print("\n--- Información de la mejora ---")
            print(f.read())
    
    consultar_mejoras(nombre_mejora)


funciones= {}
CARPETA_FUNCIONES = "funciones"
if not os.path.exists(CARPETA_FUNCIONES):
    os.makedirs(CARPETA_FUNCIONES)
for archivo_funcion in os.listdir(CARPETA_FUNCIONES):
    if archivo_funcion.endswith(".txt"):
        nombre_funcion = archivo_funcion.replace(".txt", "")
        funciones[nombre_funcion] = f"{CARPETA_FUNCIONES}/{archivo_funcion}"
def solicitar_nuevas_funciones():
    nombre_funcion = input("Ingresa la nueva función para la aplicacion: ")
    ruta = f"funciones/{nombre_funcion}.txt"
    if os.path.exists(ruta):
        print("La función propuesta ya existe. No se puede crear nuevamente.")
        return
    dpto_funcion = input("Ingresa Departamento solicitado por el cliente: ")
    archivo_funcion = f"{CARPETA_FUNCIONES}/{nombre_funcion.replace(' ', '_')}.txt"
    with open(archivo_funcion, "w") as f:
        f.write(f"Función: {nombre_funcion}\n")
        f.write(f"Departamento de la aplicacion: {dpto_funcion}\n")
    funciones[nombre_funcion] = archivo_funcion
    print("Función registrada correctamente.")
def modificar_funciones():
    nombre_funcion = input("Ingresa Nombre de la función para modificar el código de la aplicación: ")
    ruta = f"funciones/{nombre_funcion}.txt"
    if not os.path.exists(ruta):
        print("La función no existe. No se puede modificar.")
        return
    nuevo_status = input("Nuevo estado de la función: ")
    with open(funciones[nombre_funcion], "a") as f:
        f.write(f"Nuevo estado: {nuevo_status}\n")
    print("Función actualizada correctamente.")

def mostrar_funciones():
    nombre_funcion = input("Ingresa Nombre de la función para visulizar: ")

    if nombre_funcion not in funciones:
        print("Función no encontrada en la base de datos.")
        return

    with open(funciones[nombre_funcion], "r") as f:
            print("\n--- Información de la función ---")
            print(f.read())
    
    notificar_funcion(nombre_funcion)



def menu():
    while True:
        print("\n--- Amazon (Fase 2) ---")
        print("1. Crear nuevo cliente")
        print("2. Mostrar lista de clientes registrados")
        print("3. Consultar cliente")
        print("4. Actualizar cliente")
        print("5. Borrar cliente")
        print("6. Registro de mejora a la aplicacion")
        print("7. Modificacion del codigo de aplicacion")
        print("8. Mostrar mejoras registradas")
        print("9. Solicitud de nuevas funciones de la aplicacion")
        print("10. Modificacion del código de las funciones de la aplicacion")
        print("11. Mostrar funciones registradas")
        print("12. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            consultar_lista()
        elif opcion == "3":
            consultar_cliente()
        elif opcion == "4":
            actualizar_cliente()
        elif opcion == "5":
            borrar_cliente()
        elif opcion == "6":
            registrar_mejora()
        elif opcion == "7":
            modificar_codigo()
        elif opcion == "8":
            mostrar_mejoras()
        elif opcion == "9":
            solicitar_nuevas_funciones()
        elif opcion == "10":
            modificar_funciones()
        elif opcion == "11":
            mostrar_funciones()
        elif opcion == "12":
            print("Saliendo del sistema. Gracias por usar Amazon.")
            break
        else:
            print("Opción no válida. Por favor, ingresa nuevamente un numero correcto.")

menu()