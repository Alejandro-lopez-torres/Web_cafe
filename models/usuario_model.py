import MySQLdb.cursors

def obtener_usuario_por_email(mysql, email):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
    return cursor.fetchone()

def registrar_usuario(mysql, nombre, email, contrasena):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)', (nombre, email, contrasena))
    mysql.connection.commit()
    return cursor.lastrowid