from flask import request, session, redirect, url_for, render_template 
from models.usuario_model import obtener_usuario_por_email ,registrar_usuario
from models.usuario_model import registrar_usuario


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

 

def registro_controller(mysql, request):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        contrasena = request.form['contrasena']
        if obtener_usuario_por_email(mysql, email):
            error = 'El email ya está registrado.'
            return render_template('registro.html', error=error)
        else:
            registrar_usuario(mysql, nombre, email, contrasena)
            return redirect(url_for('login'))
    return render_template('registro.html')


