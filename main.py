# IMPORTAR LIBRERÍAS
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


# CONFIGURAR APLICACIÓN
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"


# CONFIGURAR PÁGINA
@application.route("/inicio")
def inicio():
    return "Hola estas en la pagina de inicio"
