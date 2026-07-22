
import sqlite3

# def conectar_f_main1(): # funcion version v.1
#     return sqlite3.connect("ventas.db")

def conectar_f_main1(): #funcion version v.2
    conexion = sqlite3.connect("ventas.db")
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tablas_f1():
    conexion = conectar_f_main1()
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


# ______________________________________________________

def agregar_prenda_f1(nombre,precio,stock):
    conexion = conectar_f_main1()
    cursor = conexion.cursor()

    cursor.execute("""
                   INSERT INTO prendas(nombre, precio, stock)
                   VALUES(?, ?, ?)
                   """,(nombre, precio,stock))
    conexion.commit()
    conexion.close()
# ______________________________________________________

def ver_prendas_f1():
    conexion = conectar_f_main1()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, precio, stock
        FROM prendas
    """)

    prendas = cursor.fetchall()# busca todos los id

    conexion.close()

    return prendas

# ______________________________________________________
def buscar_prenda_f1(id_prenda): # "Dame un ID y yo buscaré esa prenda."
    conexion = conectar_f_main1()
    cursor = conexion.cursor()

    cursor.execute("""
                   SELECT *
                   FROM prendas
                   WHERE id = ?
                   """,(id_prenda,))
    prenda = cursor.fetchone() # busca un id
    conexion.close()
    return prenda
# ______________________________________________________

def actualizar_stock_f1(id_prenda,nuevo_stock):
    conexion = conectar_f_main1()
    cursor = conexion.cursor()

    cursor.execute("""
                   UPDATE prendas
                   SET stock = ?
                   WHERE id = ?
                   """,(nuevo_stock,id_prenda))
    conexion.commit()
    conexion.close()

# ______________________________________________________

def eliminar_prenda_f1(id_prenda):
    conexion = conectar_f_main1()
    cursor = conexion.cursor()

    cursor.execute("""
                   DELETE FROM prendas
                   WHERE id = ?
""",(id_prenda))

    conexion.commit()
    conexion.close()
# ______________________________________________________

def agregar_reserva_f1(cliente, id_prenda):
    conexion = conectar_f_main1()
    cursor = conexion.cursor()
    cursor.execute("""
INSERT INTO reservas(cliente, prenda_id)
VALUES(?, ?)
""",(cliente, id_prenda))

    conexion.commit()
    conexion.close()

# ______________________________________________________

def ver_reservas_f1():
    conexion = conectar_f_main1()
    cursor = conexion.cursor()
    cursor.execute("""
    SELECT
        reservas.id,
        reservas.cliente,
        prendas.nombre
    FROM reservas
    INNER JOIN prendas
        ON reservas.prenda_id = prendas.id
""")
    reservas = cursor.fetchall()
    conexion.close()
    return reservas
# ______________________________________________________
# funciones llamando otras Funciones relacionado con opciones ll
# ______________________________________________________

def registrar_prenda_f2(): # opcion 1
    try:
        nombre = input("Nombre de la prenda: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        agregar_prenda_f1(nombre,precio,stock)
        print("\nPrenda registrad ")

    except ValueError:
        print("precio o stock invalido")
# ______________________________________________________

def mostrar_catalogo_f2(): # opcion 2

    prendas = ver_prendas_f1()

    if not prendas:
        print("No hay prensas registradas")
        return

    print("\n======Catalogo======")
    for prenda in prendas:
        print(
            f"""
ID: {prenda["id"]}
Nombre: {prenda["nombre"]}
Precio: S/. {prenda["precio"]}
Stock: {prenda["stock"]}
---------------
"""
        )
# ______________________________________________________

def buscar_prenda_f2():
    id_prenda = int(input("Ingrese el ID de la prenda: "))
    prenda = buscar_prenda_f1(id_prenda)
    if prenda is None:
        print("\nNo existe una  prenda con este ID.")
        return
    print(
        f"""
ID: {prenda["id"]}
Nombre: {prenda["nombre"]}
Precio: S/. {prenda["precio"]}
Stock: {prenda["stock"]}
---------------
""")
# ______________________________________________________

def vender_prenda_f2():
    id_prenda = int(input("ingrese el id de la prenda"))
    prenda = buscar_prenda_f1(id_prenda)

    if prenda is None:
        print("La prenda no existe")
        return

    cantidad = int(input("cantidad a vender: "))

    if cantidad > prenda["stock"]:
        print("Stock insuficiente.")
        return

    nuevo_stock = prenda["stock"] - cantidad
    actualizar_stock_f1(id_prenda,nuevo_stock)

    print("\nVenta realizada.")
# ______________________________________________________
def reponer_prenda_f2():
    id_prenda = int(input("Ingrese el id de la prenda")) # Pedir ID
    prenda = buscar_prenda_f1(id_prenda)# Buscar prenda

    if prenda is None: # ¿Existe?
        print("La prenda no existe.")
        return
    cantidad = int(input("Cantidad a reponer: ")) # Pedir cantidad
    nuevo_stock = prenda["stock"] + cantidad # Calcular nuevo stock

    actualizar_stock_f1(id_prenda,nuevo_stock) # Actualizar BD

    print("\nStock actualizado correctamente") # Mostrar mensaje
# ______________________________________________________
def eliminar_prenda_f2():
    id_prenda = int(input("Ingrese id de la prenda: "))
    prenda = buscar_prenda_f1(id_prenda)
    if prenda is None:
        print("La prenda no existe.")
        return

    print(f"""
ID: {prenda["id"]}
Nombre: {prenda["nombre"]}
Precio: S/. {prenda["precio"]}
Stock: {prenda["stock"]}
---------------
""")
    confirmar = input("Esta seguro de eliminar esta prenda? s/n: ")
    if confirmar.lower() == "s":
        eliminar_prenda_f1(id_prenda)
        print("\nPrenda eliminada correctamente")

    else:
        print("operacion cancelada")
# ______________________________________________________

def reservar_prenda_f2():
    cliente  = input("Nombre del cliente: ") # id cliente
    id_prenda = int(input("ID de la prenda: ")) # id de prenda
    prenda = buscar_prenda_f1(id_prenda)# buscamos prenda

    if prenda is None:  # existe?
        print("La prenda no existe.")
        return
    agregar_reserva_f1(cliente,id_prenda) # guardar reserva
    print("Reserva registrada correcatamente.") # confirma reserva
# ______________________________________________________

def mostrar_reservas_f2():
    reservas = ver_reservas_f1()

    if not reservas:
        print("No hay reservas registradas. ")
        return
    for reserva in reservas:
        print(f"""
ID Reserva : {reserva["id"]}
Cliente : {reserva["cliente"]}
Prenda : {reserva["nombre"]}
------------------
""")
# ______________________________________________________

def menu():
    while True:
        print("\n==========APP Fio=========")
        print("1. Agregar prenda")
        print("2. ver catalogo")
        print("3. buscar prenda")
        print("4. vender prenda")
        print("5. reponer prenda")
        print("6. eliminar prenda")
        print("7. reservar prenda")
        print("8. ver reservas")
        print("9. Salir\n")

        opcion =  input("Ingrese unaa opcion: ")

        if opcion == "1":
            registrar_prenda_f2()
        elif opcion == "2":
            mostrar_catalogo_f2()
        elif opcion == "3":
            buscar_prenda_f2()
        elif opcion == "4":
            vender_prenda_f2()
        elif opcion == "5":
            reponer_prenda_f2()
        elif opcion == "6":
            eliminar_prenda_f2()
        elif opcion == "7":
            reservar_prenda_f2()
        elif opcion == "8":
            mostrar_reservas_f2()

        elif opcion == "9":
            print("APP Closed ")
            break
        else:
            print("Opcion no valida.")
# ______________________________________________________

if __name__ == "__main__":
    crear_tablas_f1()
    menu()
