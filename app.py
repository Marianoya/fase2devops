from flask import Flask, request, jsonify
import main  # para reutilizar tu lógica actual

app = Flask(__name__)

# Ejemplo: listar clientes
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    # aquí llamas a la función que ya tengas en tu código
    # por ejemplo, si en main.py tienes algo como listar_clientes()
    clientes = main.listar_clientes()  # ajustamos al nombre real
    return jsonify(clientes)

# Ejemplo: crear cliente
@app.route("/clientes", methods=["POST"])
def crear_cliente():
    data = request.json
    # aquí llamas a tu función actual de crear cliente
    nuevo = main.crear_cliente(data)  # ajustamos al nombre real
    return jsonify(nuevo), 201

# Endpoint simple para probar que el servicio está vivo
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Fase2 DevOps API funcionando"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)