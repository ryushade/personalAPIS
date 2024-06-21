from bd import obtener_conexion

def obtener_user_por_username(username):
    conexion = obtener_conexion()
    user = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, email, password, token FROM users WHERE email = %s", (username,))
        user = cursor.fetchone()
    conexion.close()
    return user


def obtener_user_por_id(id):
    conexion = obtener_conexion()
    user = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, email, password FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
    conexion.close()
    return user

def insertar_user(username, epassword):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO users(email, password) VALUES (%s, %s)",
                       (username, epassword))
    conexion.commit()
    conexion.close()

def actualizar_token(username, token):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("update users set token = %s where email = %s ",
                       (token, username))
    conexion.commit()
    conexion.close()

