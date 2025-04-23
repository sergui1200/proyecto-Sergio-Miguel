# proyecto-Sergio-Miguel
proyecto de una API parte 1

---------------------------------------------------------------------------------
### ESQUEMA GENERAL DE LA API
---------------------------------------------------------------------------------
## ESQUEMA DEL PROYECTO
clase dam1/
├── README.md
├── LICENSE
├── AUTHORS
├── .gitignore
├── src/
│   ├── templates/
│   │   ├── inicio.html
│   │   ├── eliminar.html
│   │   ├── insertar.html
│   ├── main.py
├── instalacion.sql
├── Database.db

# IMPORTAR LIBRERÍAS
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


# CREAR BD
def init_db():
    conn = sqlite3.connect('Sergio_alumnos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE dam1(
id INT PRIMARY KEY,
nombre VARCHAR(10),
apellidos TEXT,
asignaturas TEXT,
media INT,
aprobado BOOLEAN
);
''')
    conn.commit()
    conn.close()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/mostrar_todo', methods=['GET'])
def mostrar_todo():
    conn = sqlite3.connect('Sergio_alumnos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dam1')
    dam1 = cursor.fetchall()
    conn.close()
    return jsonify(dam1)

@app.route('/mostrar', methods=['GET'])
def mostrar_con_argumentos():
    id = request.args.get('id')
    conn = sqlite3.connect('Sergio_alumnos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dam1 WHERE id=?', (id,))
    dam1 = cursor.fetchall()
    conn.close()
    return jsonify(dam1)

@app.route('/insertar', methods=['POST'])
def insertar():
    datos = request.json
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dam1 VALUES (1,'Sergio','Buendia Colao','PRO ED INGLES',5,TRUE),(2,'Miguel','Platon cano','PRO ED INGLES',4,FALSE),(3,'Pablo','Paraiso','PRO BD XML FOL ED INGLES',7,TRUE),(4,'Jorge','CASAS','PRO BD XML FOL ED INGLES',9,TRUE);',
                   (datos['id'], datos['nombre'], datos['apellidos'], datos['asignaturas'], datos['media'], datos['aprobado']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Coche insertado correctamente'})

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    id = request.args.get('id')
    conn = sqlite3.connect('Sergio_alumnos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dam1 WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Coche eliminado correctamente'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)



## HTML

## SQL
CREATE TABLE dam1(
id INT PRIMARY KEY,
nombre VARCHAR(10),
apellidos TEXT,
asignaturas TEXT,
media INT,
aprobado BOOLEAN
);




