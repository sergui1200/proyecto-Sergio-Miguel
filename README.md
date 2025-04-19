# proyecto-Sergio-Miguel
proyecto de una API parte 1

---------------------------------------------------------------------------------
### ESQUEMA GENERAL DE LA API
---------------------------------------------------------------------------------
## ESQUEMA DEL PROYECTO
superdeportivos/
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

## PYTHON ESTRUCTURA
from flask import Flask, render_template, request, jsonify
import sqlite3

api = Flask(__name__)

# Crear la base de datos
def init_db():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS superdeportivos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        marca TEXT NOT NULL,
                        modelo TEXT NOT NULL,
                        velocidad_maxima INTEGER NOT NULL,
                        precio REAL NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/mostrar_todo', methods=['GET'])
def mostrar_todo():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM superdeportivos')
    coches = cursor.fetchall()
    conn.close()
    return jsonify(coches)

@app.route('/mostrar', methods=['GET'])
def mostrar_con_argumentos():
    marca = request.args.get('marca')
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM superdeportivos WHERE marca=?', (marca,))
    coches = cursor.fetchall()
    conn.close()
    return jsonify(coches)

@app.route('/insertar', methods=['POST'])
def insertar():
    datos = request.json
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO superdeportivos (marca, modelo, velocidad_maxima, precio) VALUES (?, ?, ?, ?)',
                   (datos['marca'], datos['modelo'], datos['velocidad_maxima'], datos['precio']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Coche insertado correctamente'})

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    coche_id = request.args.get('id')
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM superdeportivos WHERE id=?', (coche_id,))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Coche eliminado correctamente'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

## HTML

## SQL
CREATE TABLE superdeportivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    velocidad_maxima INTEGER NOT NULL,
    precio REAL NOT NULL
);



