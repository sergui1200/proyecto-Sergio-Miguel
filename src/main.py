# IMPORTAR LIBRERÍAS
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection

# configuracion del proyecto
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

# PAGINAS
@application.route("/inicio",methods =["HTML"])
def inicio():
    return "hola bienvenido a nuestro proyecto"

@application.route("/nombres")
def nombres():
    nombres = "Sergio, Miguel"
    return nombres

@application.route("/apellidos")
def apellidos():
    apellidos = "Buendia Colao, Platon Cano"
    return apellidos

@application.route("/id")
def id():
    ids = "1,2"
    return ids
@application.route("/final")
def final():
    return "este es el final del proyecto"
# MOSTRAR 
@application.route("/mostrar", methods = ["GET"])
def mostrar():
    conexion = SQLiteConnection("Sergio_alumnos.db")
    datos = conexion.execute_query("SELECT * FROM dam1")
    return datos
# METODO DELETE
@application.route("/borrar", methods = ["DELETE"])
def borrar():
    conexion = SQLiteConnection("Sergio_alumnos.db")
    datos = conexion.execute_query("DELETE FROM dam1 WHERE nota= 'media';")
    return datos
# METODO INSERT
@application.route("/Insertar", methods = ["POST"])
def Insertar():
    conexion = SQLiteConnection("Sergio_alumnos.db")
    datos = conexion.execute_query("INSERT INTO dam1 VALUES (1,'Sergio','Buendia Colao','PRO ED INGLES',5,TRUE),(2,'Miguel','Platon cano','PRO ED INGLES',4,FALSE),(3,'Pablo','Paraiso','PRO BD XML FOL ED INGLES',7,TRUE),(4,'Jorge','CASAS','PRO BD XML FOL ED INGLES',9,TRUE);")
    return datos


