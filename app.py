from flask import Flask, request, jsonify
import main

app = Flask(__name__)

# ---------------- CLIENTES ----------------
@app.route("/clientes", methods=["POST"])
def crear_cliente():
    data = request.json
    nombre = data.get("nombre")
    servicio = data.get("servicio")
    resultado = main.api_crear_cliente(nombre, servicio)
    return jsonify(resultado)

@app.route("/clientes", methods=["GET"])
def listar_clientes():
    resultado = main.api_listar_clientes()
    return jsonify(resultado)

@app.route("/clientes/<nombre>", methods=["GET"])
def consultar_cliente(nombre):
    resultado = main.api_consultar_cliente(nombre)
    return jsonify(resultado)

@app.route("/clientes/<nombre>", methods=["DELETE"])
def borrar_cliente(nombre):
    resultado = main.api_borrar_cliente(nombre)
    return jsonify(resultado)


# ---------------- MEJORAS ----------------
@app.route("/mejoras", methods=["POST"])
def registrar_mejora():
    data = request.json
    nombre = data.get("nombre")
    servicio = data.get("servicio")
    resultado = main.api_registrar_mejora(nombre, servicio)
    return jsonify(resultado)

@app.route("/mejoras/<nombre>", methods=["GET"])
def mostrar_mejora(nombre):
    resultado = main.api_mostrar_mejora(nombre)
    return jsonify(resultado)

@app.route("/mejoras/<nombre>", methods=["PUT"])
def modificar_mejora(nombre):
    data = request.json
    nuevo_estado = data.get("estado")
    resultado = main.api_modificar_mejora(nombre, nuevo_estado)
    return jsonify(resultado)


# ---------------- FUNCIONES ----------------
@app.route("/funciones", methods=["POST"])
def registrar_funcion():
    data = request.json
    nombre = data.get("nombre")
    departamento = data.get("departamento")
    resultado = main.api_registrar_funcion(nombre, departamento)
    return jsonify(resultado)

@app.route("/funciones/<nombre>", methods=["GET"])
def mostrar_funcion(nombre):
    resultado = main.api_mostrar_funcion(nombre)
    return jsonify(resultado)

@app.route("/funciones/<nombre>", methods=["PUT"])
def modificar_funcion(nombre):
    data = request.json
    nuevo_estado = data.get("estado")
    resultado = main.api_modificar_funcion(nombre, nuevo_estado)
    return jsonify(resultado)


# ---------------- HEALTH CHECK ----------------
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "API funcionando"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)