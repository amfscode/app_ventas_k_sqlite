

import sqlite3

def conectar():
    return sqlite3.connect("ventas.db")

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS prendas (
                   id  INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   precio REAL NOT NULL,
                   stock INTEGER NOT NULL
                   )
                   """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS reservas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente TEXT NOT NULL,
                   prenda_id INTEGER  NOT NULL,
                   FOREIGN KEY (prenda_id) REFERENCES prendas(id)
                   )
                   """)

    conexion.commit()
    conexion.close()

crear_tablas()