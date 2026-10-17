from flask import Flask

app = Flask(__name__)


def saludo(nombre="mundo"):
    return f"Hola, {nombre}!"


def obtener_mensaje(texto="mensaje"):
    return f"Mensaje: {texto}"


@app.route("/")
def index():
    return saludo()


@app.route("/hola")
def hola():
    return saludo("mundo")


@app.route("/saludo/<nombre>")
def saludo_personalizado(nombre):
    return saludo(nombre)


@app.route("/mensaje")
def mensaje():
    return obtener_mensaje("Este es un mensaje de prueba")


if __name__ == "__main__":
    app.run(debug=True)
