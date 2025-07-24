from flask import session, redirect, url_for, render_template
from models.usuario_model import obtener_usuario_por_email

def login_controller(mysql, request):
    error = None
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        usuario = obtener_usuario_por_email(mysql, email)
        if usuario and usuario['contrasena'] == contrasena:
            session['usuario_id'] = usuario['id']
            session['nombre'] = usuario['nombre']
            return redirect(url_for('index'))
        else:
            error = 'Email o contraseña incorrectos.'
    return render_template('login.html', error=error)