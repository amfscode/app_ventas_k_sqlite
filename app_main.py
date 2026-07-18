
import sqlite3

# def conectar(): #funcion version v.1
#     return sqlite3.connect("ventas.db")

def conectar(): #funcion version v.2
    conexion = sqlite3.connect("ventas.db")
    conexion.row_factory = sqlite3.Row
    return conexion

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

# crear_tablas()
# agregar_prenda("fio",100,2)

def ver_prendas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, precio, stock
        FROM prendas
    """)

    prendas = cursor.fetchall()# busca todos los id

    conexion.close()

    return prendas

def buscar_prenda(id_prenda): # "Dame un ID y yo buscaré esa prenda."
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
                   SELECT *
                   FROM prendas
                   WHERE id = ?
                   """,(id_prenda,))
    prenda = cursor.fetchone() # busca un id
    conexion.close()
    return prenda
# ____________________________________

# probando
# crear_tablas()
# agregar_prenda("Polo negro", 50, 10)

prendas = ver_prendas()
for prenda in prendas:
    print(
        f"Precio: S/. {prenda['precio']} | "
        f"Stock: {prenda['stock']}"
    )

crear_tablas()

prenda = buscar_prenda(1)

print(prenda)

print(prenda["id"])
print(prenda["nombre"])
print(prenda["precio"])
print(prenda["stock"])

#mejorando ver_prendas con un bucle
# for prenda in prendas:

# accediendo a cada dato
# for prenda in prendas:
#     print("ID: ",prenda[0])
#     print("Nombre: ",prenda[1])
#     print("Precio: ",prenda[2])
#     print("Stock: ",prenda[3])
#     print("___")
