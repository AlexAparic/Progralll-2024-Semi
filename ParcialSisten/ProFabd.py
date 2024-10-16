import mysql.connector
from conexion import obtener_conexion  # Asegúrate de que este archivo tenga la lógica de conexión a la BD

def agregar_usuario(nombre, direccion, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO usuarios (nombre, direccion, telefono) VALUES (%s, %s, %s)"
    valores = (nombre, direccion, telefono)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al agregar usuario: {err}")
    finally:
        cursor.close()
        conexion.close()


def listar_usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        return usuarios
    except mysql.connector.Error as err:
        print(f"Error al listar usuarios: {err}")
        return []
    finally:
        cursor.close()
        conexion.close()



def actualizar_usuario(id, nombre, direccion, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE usuarios
        SET nombre = %s, direccion = %s, telefono = %s
        WHERE id = %s
    """
    valores = (nombre, direccion, telefono, id)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al actualizar usuario: {err}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_usuario(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM usuarios WHERE id=%s"
    try:
        cursor.execute(sql, (id,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al eliminar usuario: {err}")
    finally:
        cursor.close()
        conexion.close()


# Método para buscar productos por nombre o categoría
def buscar_usuarios(busqueda):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = """
        SELECT * FROM usuarios 
        WHERE nombre LIKE %s 
        OR direccion LIKE %s 
        OR telefono LIKE %s
    """
    try:
        valores_busqueda = ('%' + busqueda + '%', '%' + busqueda + '%', '%' + busqueda + '%')
        cursor.execute(sql, valores_busqueda)
        usuarios = cursor.fetchall()
        return usuarios
    except mysql.connector.Error as err:
        print(f"Error al buscar usuarios: {err}")
        return []
    finally:
        cursor.close()
        conexion.close()
