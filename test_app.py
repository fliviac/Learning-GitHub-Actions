from app import app, saludo, obtener_mensaje


def test_saludo_default():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hola, mundo!"


def test_saludo_personalizado():
    client = app.test_client()
    response = client.get("/saludo/Fabio")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hola, Fabio!"


def test_hola_route():
    client = app.test_client()
    response = client.get("/hola")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hola, mundo!"


def test_mensaje_route():
    client = app.test_client()
    response = client.get("/mensaje")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Mensaje: Este es un mensaje de prueba"


def test_helper_functions():
    assert saludo() == "Hola, mundo!"
    assert saludo("Ana") == "Hola, Ana!"
    assert obtener_mensaje("Prueba") == "Mensaje: Prueba"
