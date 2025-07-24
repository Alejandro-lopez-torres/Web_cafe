import MySQLdb.cursors

def obtener_usuario_por_email(mysql, email):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
    return cursor.fetchone()