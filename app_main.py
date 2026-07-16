
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

# crear_tablas()

# bloque para agregar tablas(filas a tablas existentes)

def agregar_prenda(nombre,precio,stock):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
                   INSERT INTO prendas(nombre, precio, stock)
                   VALUES(?, ?, ?)
                   """,(nombre, precio,stock))
    # conexion.commit()
    conexion.close()

# agregando un valores a prendas

crear_tablas()
agregar_prenda("fio",100,2)

def ver_prendas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, precio, stock
        FROM prendas
    """)

    prendas = cursor.fetchall()

    conexion.close()

    return prendas

# probando
crear_tablas()

agregar_prenda("Polo negro", 50, 10)

prendas = ver_prendas()

print(prendas)
