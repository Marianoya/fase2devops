#Version1.1.
import os
import token
import requests

print("TOKEN:", os.getenv("GITHUB_TOKEN"))

def notificar_consulta(nombre_cliente):
    token = os.getenv("GITHUB_TOKEN")
    url = "https://api.github.com/repos/Marianoya/actividad2_devops/dispatches"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "event_type": "consulta_cliente",
        "client_payload": {
            "cliente": nombre_cliente
        }
    }
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


def menu():
    while True:
        print("\n--- Sistema Axanet (Actividad 2) ---")
        print("1. Crear nuevo cliente")
        print("2. Mostrar lista de clientes registrados")
        print("3. Consultar cliente")
        print("4. Actualizar cliente")
        print("5. Borrar cliente")
        print("6. Salir")

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
            print("Saliendo del sistema. Gracias por usar Axanet.")
            break
        else:
            print("Opción no válida. Por favor, ingresa nuevamente un numero correcto.")


menu()