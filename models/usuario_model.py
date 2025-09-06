import MySQLdb.cursors

def obtener_usuario_por_email(mysql, email):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
    return cursor.fetchone()

def registrar_usuario(mysql, nombre, email, contrasena, telefono, direccion):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        'INSERT INTO usuarios (nombre, email, contrasena, telefono, direccion) VALUES (%s, %s, %s, %s, %s)',
        (nombre, email, contrasena, telefono, direccion)
    )
    mysql.connection.commit()
    return cursor.lastrowid